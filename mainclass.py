from time import  sleep
from hirajBasedObjects import (
    HirajBase,
    PostObject ,
    LeadObject ,
    RequestKeys ,
    )

from Packages import  (
    QObject,
    pyqtSignal )


class Hiraj(QObject):
    class FastLevelFlags():
        Normal = 'Normal'
        High = 'High'
        SuperFast = 'SuperFast'
        All = [Normal,High,SuperFast]

    LeadSignal = pyqtSignal(dict)
    msg = pyqtSignal(str)
    

    def __init__(
        self ,
        FastLevel:FastLevelFlags = FastLevelFlags.Normal
        ) -> None:
        self.HirajBase = HirajBase()
        super().__init__()
        self.HirajBase.msg.connect(self.msg.emit)
        self.FastLevel = FastLevel
        

    def Search(self,limitPage:int=None,comments:HirajBase.Flags= HirajBase.Flags.No,**kwargs):
        endrange = limitPage if limitPage != None else 200
        for page in range(1,endrange):
            kwargs[RequestKeys.Search.page] = page
            PostsObj = self.HirajBase.Search(**kwargs)
            for post in PostsObj.Posts :
                print(post.id)
                Lead = LeadObject(post,BaseClass=self.HirajBase)
                if Lead.PhoneNumber != '' :
                    self.LeadSignal.emit(Lead.dictOfObject)
                    print(Lead.dictOfObject)
                if comments == HirajBase.Flags.Yes :
                    self.Comments(post)


    
    def Comments(self,post:PostObject):
        commentsObj = self.HirajBase.Comments(post)
        for author in commentsObj.CommenterNames :
            PostsObject = self.HirajBase.FetchAds(**{RequestKeys.FetchAds.authorUsername:author})
            for post in PostsObject.Posts:
                Lead = LeadObject(post,self.HirajBase)
                if Lead.PhoneNumber != '':
                    self.LeadSignal.emit(Lead.dictOfObject)
                    print(Lead.dictOfObject)
                    break
            

    def Similar(self,numbersList:list ,comments:HirajBase.Flags = HirajBase.Flags.No):
        idslist = [self.HirajBase.Data.Search('ContactsData','contactMobile',number,0) for number in numbersList]
        for id in idslist:
            if id != None :
                postsObj = self.HirajBase.SimilarPosts(id)
                for post in postsObj.Posts:
                    Lead = LeadObject(post,self.HirajBase)
                    if Lead.PhoneNumber != '' :
                        self.LeadSignal.emit(Lead.dictOfObject)
                        print(Lead.dictOfObject)
                      

# h = Hiraj()
# h.Search(limitPage=2,**{
#         RequestKeys.Search.tag:"مستلزمات شخصية",
#         RequestKeys.Search.cities:[
#                 "الرياض"
#             ],
#         RequestKeys.Search.search:"ساعة"
#     })
