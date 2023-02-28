from time import  sleep
from hirajBasedObjects import (
    HirajBase,
    PostObject ,
    LeadObject ,
    RequestKeys ,
    DataTableFlags
    )

from Packages import  (
    QObject,
    pyqtSignal )

# class FastLevelFlags():
#     Normal = 'Normal'
#     High = 'High'
#     SuperFast = 'SuperFast'
#     All = [Normal,High,SuperFast]


class Hiraj(QObject):

    LeadSignal = pyqtSignal(dict)
    msg = pyqtSignal(str)
    status = pyqtSignal(str)

    def __init__(
        self ,
        ) -> None:
        super().__init__()
        self.HirajBase = HirajBase()
        # self.HirajBase.status.connect(self.status.emit)
        self.HirajBase.msg.connect(self.msg.emit)
        

    def Search(self,limitPage:int=None,comments:HirajBase.Flags= HirajBase.Flags.No,**kwargs):
        endrange = limitPage if limitPage != None else 200
        for page in range(1,endrange):
            print(f"Page Num -> {page}")
            self.status.emit(f"Scrape Page -> {page}")
            kwargs[RequestKeys.Search.page] = page
            try :
                PostsObj = self.HirajBase.Search(**kwargs)
                for post in PostsObj.Posts :
                    if post.isNew :
                        self.status.emit(f"Scraped Post with ID : {post.id}")
                        Lead = LeadObject(post,BaseClass=self.HirajBase)
                        print(f"Phone -> {Lead.PhoneNumber}")
                        if Lead.PhoneNumber != '' and Lead.isNew :
                            self.LeadSignal.emit(Lead.dictOfObject)
                        if comments == HirajBase.Flags.Yes :
                            self.Comments(post)
            except Exception as e :
                self.msg.emit(f"Error in Internet connection -> {e}")
                break
                

    
    def Comments(self,post:PostObject):
        commentsObj = self.HirajBase.Comments(post)
        for author in commentsObj.CommenterNames :
            PostsObject = self.HirajBase.FetchAds(**{RequestKeys.FetchAds.authorUsername:author})
            self.status.emit(f"Scraped Commenter From Post ID : {post.id}")
            for post in PostsObject.Posts:
                self.status.emit(f"Scraped Commenter Post with ID : {post.id}")
                Lead = LeadObject(post,self.HirajBase)
                if Lead.PhoneNumber != '' and Lead.isNew :
                    self.LeadSignal.emit(Lead.dictOfObject)
                    break
            

    def Similar(self,numbersList:list ,comments:HirajBase.Flags = HirajBase.Flags.No):
        idslist = [self.HirajBase.Data.Search('ContactsData','contactMobile',number,0) for number in numbersList]
        for id in idslist:
            if id != None :
                self.status.emit(f"Scraped in {numbersList[idslist.index(id)]}")
                try:
                    postsObj = self.HirajBase.SimilarPosts(id)
                    for post in postsObj.Posts:
                        if post.isNew :
                            self.status.emit(f"Scraped Similar Posts Like ID : {post.id}")
                            Lead = LeadObject(post,self.HirajBase)
                            if Lead.PhoneNumber != '' and Lead.isNew :
                                self.LeadSignal.emit(Lead.dictOfObject)
                                print(Lead.dictOfObject)
                            if comments == HirajBase.Flags.Yes :
                                self.Comments(post)
                except Exception as e :
                    self.msg.emit(f"Error in Internet connection -> {e}")
                    break