from time import  sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from typing import List


class Hiraj():
    def __init__(self) -> None:
        pass
        

    def start_browser(self,hidebrowser:bool):
        option = Options()
        option.headless = hidebrowser
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        option.add_argument('--disable-logging')
        self.driver =webdriver.Chrome(ChromeDriverManager().install(),options=option)
        self.driver.maximize_window()
        self.driver.get("https://haraj.com.sa/")
        self.wait = WebDriverWait(self.driver, 100)    
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))

    def wait_elm(self,val:str,by:str=By.XPATH,timeout:int=30)->WebElement:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.wait.until(EC.presence_of_element_located(arg))

    def wait_elms(self,val:str,by:str=By.XPATH,timeout:int=30)->List[WebElement]:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        elments = self.wait.until(EC.presence_of_all_elements_located(arg))
        return elments

    # def wait_elm_text(self,val:str,by:str=By.XPATH,timeout:int=30)-> WebElement:
    #     self.wait = WebDriverWait(self.driver, timeout=timeout)
    #     arg = (by,val)
    #     element = self.wait.until(EC.text_to_be_present_in_element(arg))
    #     return element


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
            lengthofposts = len(posts)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait_elm("//button[@id='more']",timeout=6).click()
                sleep(1)
                posts = self.driver.find_elements(By.XPATH,"//div[@class='postTitle']/a")
                if lengthofposts == len(posts):
                    break
            except Exception as e :
                posts = self.driver.find_elements(By.XPATH,"//div[@class='postTitle']/a")
                break
        posts = self.driver.find_elements(By.XPATH,"//div[@class='postTitle']/a ")
        for elm in posts:
            link = elm.get_attribute("href")
            links.append(link)
        return links
            

    def scrape_info(self)->list:
        try:
            username = self.wait_elm("//span[@class='author']").text
            date = self.wait_elm("//span[@id='post_time']/span").text
            location = self.wait_elm("//span[@class='city']").text
            try:
                self.wait_elm("//button[@type='button']").click()
                phone = self.wait_elm("/html/body/div/div/div[3]/div[1]/div[1]/div[2]/div/span/div/div[2]/div/div/a[2]/div[2]").text
                self.wait_elm("//button[@id='close_btn']",timeout=3).click()
                phone = f"{phone}"
                if "05" not in phone:
                    phone = None
            except:
                phone = None
        except:
            username = None
            date = None
            location = None
            phone=None
        info = [username,phone,location,date,str(datetime.now())]
        return info
    
    def scrape_comments_users(self)->list:
        # self.driver.execute_script("""
        # h = document.getElementsByClassName("blue_btn");
        # for (let i = 0; i <10 ; i++) {
        #     if (h[0].textContent == 'تحميل ردود أقدم'){
        #         h[0].click()
        # } else {
        #     break
        # }
        # };
        # """)         
        try:
            author = self.wait_elm("//span[@class='author']",timeout=3).text
            comments_user = self.wait_elms("//span[@class='username_wrapper']/span/a",timeout=3)
            comments_users = [x.text for x in comments_user]       
            result = list(dict.fromkeys(list(filter( lambda user:user != author,comments_users))))
            #print(result)
        except Exception as e :
            result = None
        return result

    def have_ads(self):
        try:
            self.wait_elm("//div[@class='postTitle']",timeout=3)
            have = True
        except:
            have = False
        return have
        
    def get_phone(self):
        try:
            self.wait_elm("//*[@class='contact_btn_wrapper']",timeout=3).click()
            phones = self.wait_elm("//div[@class='contacts_wrpper']").find_element(By.TAG_NAME,"a").get_attribute("href").replace("tel:","")
            return phones
        except:
            pass


    def get_title(self)->str:
        return self.wait_elm("//div[@class='post_header_wrapper']/h1",timeout=3).text

            

    def scrape_user_info(self,user):
        self.driver.get(f"https://haraj.com.sa/users/{user}")#
        phone = self.get_phone()
        if phone != None:
            return [user ,phone , "" , f"{datetime.now()}","comment"]
        else:
            have = self.have_ads()
            #print(have)
            if have:
                links = [link.get_attribute("href") for link in self.wait_elms("//div[@class='postTitle']/a",timeout=3)]
                for link in links :
                    self.driver.get(link)
                    info = self.scrape_info()
                    if info[1] == None:
                        pass
                    elif "5" in info[1] :
                        phone = info[1]
                        break
                return info+["comment"]       
            else:
                return [user , None ,"",f"{datetime.now()}","comment"]
        

    def exit(self):
        try:
            self.driver.quit()
        except:
            pass
        #self.driver.close()



# h = Hiraj()
# h.start_browser(hidebrowser=True)
# h.driver.get("https://haraj.com.sa/1198459032/%D9%85%D8%B2%D8%B1%D8%B9%D8%A9_%D9%84%D9%84%D8%A8%D9%8A%D8%B9/")
# re = h.scrape_comments_users()
# print(re)

# j = [['احمد 2021 1476757', '0508232625', 'الطايف', 'تحديث قبل يوم و 5 ساعة', '2022-10-06 12:29:59.262111'], [['عبدالمنعم عبدالله 2012', '0557930122',
# 'الشرقيه', 'تحديث الآن', '2022-10-06 12:30:06.622847', 'comment']]]
