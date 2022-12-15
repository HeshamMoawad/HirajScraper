from time import  sleep
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from typing import List
from MyPyQt5 import BaseScrapingClassQt5 , Validation


class Hiraj(BaseScrapingClassQt5):
    def wait_elm(self,val:str,by:str=By.XPATH,timeout:int=5)->WebElement:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.wait.until(EC.presence_of_element_located(arg))

    def wait_elms(self,val:str,by:str=By.XPATH,timeout:int=30)->List[WebElement]:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        elments = self.wait.until(EC.presence_of_all_elements_located(arg))
        return elments

    def search(self,keyword:str,**kwargs):
        if "tagname" and "city" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}?&tag={kwargs['tagname']}")
        elif "city" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}")
        elif "tagname" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}?&tag={kwargs['tagname']}")
        else:
            self.driver.get(f"https://haraj.com.sa/search/{keyword}")


    def scrape_links(self,limit:int)->list:
        posts = []
        links = []
        lengthofposts = None
        while len(posts) < limit :
            print(f"{len(posts) < limit} while loop in scrape_links")
            lengthofposts = len(posts)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait_elm("//button[@data-testid='posts-load-more']",timeout=6).click()
                sleep(1)
                posts = self.driver.find_elements(By.XPATH,"//a[@data-testid='post-title-link']")
                if lengthofposts == len(posts):
                    print(f"Breaked in while loop {lengthofposts == len(posts)}")
                    break
            except Exception as e :
                posts = self.driver.find_elements(By.XPATH,"//a[@data-testid='post-title-link']")
                print(f"Breaked in Exception {e}")
                break
        posts = self.driver.find_elements(By.XPATH,"//a[@data-testid='post-title-link']")
        for elm in posts:
            link = elm.get_attribute("href")
            links.append(link)
        return links
            

    def exist(self,table,column,val):
        self.cur.execute(f"""SELECT * FROM {table} WHERE {column} = '{val}'; """)
        return True if self.cur.fetchall() != [] else False

    def add_to_db(self,table,**kwargs):
        try:
            self.cur.execute(f"""
            INSERT INTO {table} {str(tuple(kwargs.keys())).replace("'","")}
            VALUES {tuple(kwargs.values())}; 
            """)
            self.con.commit()
        except Exception as e:
            print(f"\n{e} \nError in Database \n")

    def get_Phone(self)->str:
        self.wait_elm('//button[@data-testid="post-contact"]').click()
        sleep(3)
        phone = self.wait_elm('//a[@data-testid="contact_mobile"]//div[@dir="ltr"]').text
        self.wait_elm('//*[@data-icon="times"]').click()
        return phone

    def get_Commenter_Info(
        self,
        link,
        ):
        self.driver.get(link)
        try:
            self.wait_elm('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div/button/span').click()
            phone = [x.text for x in self.wait_elms('//strong[@class="mb-1.5"]') if '5' in x.text]
            
            print(f'\n line 92 {phone}')
        except Exception as e :
            print(e)
            try :
                for elm in self.wait_elms('//a[@data-testid="post-title-link"]',timeout=3):
                    link = elm.get_attribute('href')
                    con = self.get_Ad_Info(link,False)
                    if con:
                        break
            except Exception as e :
                print("No ads in this user")
                pass 
        

    def get_Ad_Info(
        self,
        link:str,
        scrapeComent:bool ,
        ):
        self.driver.get(link)
        postTitle = self.wait_elm('//h1[@data-testid="post_title"]').text
        postID = self.driver.current_url.replace("https://haraj.com.sa/","").split("/")[0]
        if not self.exist(
            table = "maindata",
            column = "PostID",
            val = postID
        ):
            author = self.wait_elm('//a[@data-testid="post-author"]').text
            city = self.wait_elm('//span[@class="city"]').text
            article = self.wait_elm('//article[@data-testid="post-article"]').text
            phoneNumber = self.get_Phone()
            lead = {
                'PostID':int(postID) ,
                'Author' : author ,
                'PhoneNumber' : phoneNumber ,
                'PostTitle' : postTitle ,
                'City' : city ,
                'Article' : article ,
                'date' : f'{datetime.now().now()}',
            }
            self.add_to_db(
                'maindata',
                **lead
                )
            print(lead)
            if '5' in phoneNumber and not self.exist(table='leads',column='PhoneNumber',val = phoneNumber) :
                self.add_to_db(
                    'leads',
                    **lead
                )
                valid = Validation.Numbers(phoneNumber)
                print(valid.saudiNumberCountryCode())
                self.LeadSignal.emit([
                    author,
                    valid.saudiNumberCountryCode() ,
                    city ,
                ])

            if scrapeComent :
                try:
                    comments = self.wait_elms('//a[@class="ml-2"]',timeout=3)
                    comments = [x.get_attribute('href') for x in comments]
                    result = []
                    comments = [result.append(x) for x in comments if x not in result]
                    for link in result :
                        self.get_Commenter_Info(link)
                except Exception as e :
                    pass
            return True if '5' in phoneNumber else False
        else :
            return True
        


