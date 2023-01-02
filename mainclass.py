from time import  sleep
from datetime import datetime
from MyPyQt5 import BaseScrapingClassQt5 , Validation , DataBase


class Hiraj(BaseScrapingClassQt5,DataBase):
    def __init__(self, url: str, loginElementXpath: str, headless: bool = False, darkMode: bool = False, userProfile: str = "Guest") -> None:
        DataBase().__init__()
        super().__init__(url, loginElementXpath, headless, darkMode, userProfile)

    def search(self,keyword:str,**kwargs):
        if "tagname" and "city" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}?&tag={kwargs['tagname']}")
            print(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}?&tag={kwargs['tagname']}")
        elif "city" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}")
            print(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}")
        elif "tagname" in kwargs.keys():
            self.driver.get(f"https://haraj.com.sa/search/{keyword}?&tag={kwargs['tagname']}")
            print(f"https://haraj.com.sa/search/{keyword}?&tag={kwargs['tagname']}")
        else:
            self.driver.get(f"https://haraj.com.sa/search/{keyword}")
            print(f"https://haraj.com.sa/search/{keyword}")


    def scrape_links(self,limit:int)->list:
        links = []
        oldlen = 0
        while True : 
            oldlen = len(links)
            self.NormalScroll()
            try:
                self.wait_elm('//button[@data-testid="posts-load-more"]',timeout=3).click()
            except Exception as e :
                print("No Button More Found --- ")
            sleep(3)
            self.NormalScroll()
            try:
                posts = self.wait_elms('//a[@data-testid="post-title-link"]',timeout=5)
            except Exception as e :
                posts = []
                print("\nNo ADS Founded ----------- \n")
            links = [x.get_attribute('href') for x in posts]
            if len(links) >= limit or oldlen == len(links):
                print(f"Breaked succecfully lenlinks = {len(links)} && oldlen = {oldlen} && limit = {limit}")
                break
            print(len(links))
        return links


    def get_Phone(self)->str:
        self.wait_elm('//button[@data-testid="post-contact"]',timeout= 8 ).click()
        sleep(3)
        phone = self.wait_elm('//a[@data-testid="contact_mobile"]//div[@dir="ltr"]' , timeout= 8).text
        self.wait_elm('//*[@data-icon="times"]',timeout=8).click()
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
        try:
            postTitle = self.wait_elm('//h1[@data-testid="post_title"]',timeout=10).text
            con = True
        except Exception as e :
            con = False
        if con :
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
        


