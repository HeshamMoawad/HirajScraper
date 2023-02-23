from time import  sleep
import json , requests , json
from hirajBasedObjects import (
    HirajBase,
    PostObject ,
    LeadObject
    )
from Packages import  (
    DataBase , 
    QObject,
    pyqtSignal ,
    DateOperations ,
    Generator , 
    typing
    )




class HirajSlots(QObject):
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
        

    def Search(self,comments:HirajBase.Flags= HirajBase.Flags.No,**kwargs):
        PostsObj = self.HirajBase.Search(**kwargs)
        for post in PostsObj.Posts :
            post.addToDataBase()
            Lead = LeadObject(post,BaseClass=self.HirajBase)
            if Lead.PhoneNumber != '' :
                self.LeadSignal.emit(Lead.dictOfObject)
                print(Lead.dictOfObject)
            if comments == HirajBase.Flags.Yes :
                self.Comments(post)


    
    def Comments(self,post:PostObject):
        commentsObj = self.HirajBase.Comments(post)
        for author in commentsObj.CommenterNames :
            PostsObject = self.HirajBase.FetchAds(**{self.HirajBase.RequestKeys.FetchAds.authorUsername:author})
            for post in PostsObject.Posts:
                Lead = LeadObject(post,self.HirajBase)
                if Lead.PhoneNumber != '':
                    self.LeadSignal.emit(Lead.dictOfObject)
                    print(Lead.dictOfObject)
                    break
            



    #     self.TranslateAdsInfo(ads=AdsData['Result'],breakwhenphone=False,comments=comments)
            



    # def TranslateAdsInfo(self, ads ,breakwhenphone:bool = False , comments:HirajBase.Flags = HirajBase.Flags.No):
    #     for Ad in ads:
    #         Lead = {}
    #         self.HirajBase.setCreator(
    #         AdID = Ad[HirajBase.ResponseKeys.Search.id] ,
    #         AdCreatorID = Ad[HirajBase.ResponseKeys.Search.authorId] ,
    #         AdCreatorUsername = Ad[HirajBase.ResponseKeys.Search.authorUsername]
    #     )
    #         self.HirajBase.Profile(Ad[HirajBase.ResponseKeys.Search.authorId])
    #         Lead['UserName'] = Ad[HirajBase.ResponseKeys.Search.authorUsername]
    #         Lead['Title'] = Ad[self.HirajBase.ResponseKeys.FetchAds.title]
    #         Lead['PhoneNumber'] = self.HirajBase.PostContact(Ad[self.HirajBase.ResponseKeys.FetchAds.id])
    #         Lead['LastSeen'] = str(self.HirajBase.Date.translateTimeFromStampToDate(stamp = float(self.HirajBase.User(Ad[HirajBase.ResponseKeys.Search.authorUsername]))))
    #         if Lead['PhoneNumber'] != '' :
    #             self.LeadSignal.emit(Lead)
    #             print(Lead)
    #             if breakwhenphone :
    #                 break
    #         if comments == HirajBase.Flags.Yes :
    #             self.Comments(Ad[HirajBase.ResponseKeys.Search.id])

    # def Similar(self,numbersList:list ,comments:HirajBase.Flags = HirajBase.Flags.No):
    #     idslist = [self.HirajBase.Data.Search('ContactsData','contactMobile',number,0) for number in numbersList ]
    #     for id in idslist:
    #         if id != None :
    #             ads = self.HirajBase.SimilarPosts(id)
    #             self.TranslateAdsInfo(ads,comments,breakwhenphone=False)
            
        



# h = HirajSlots()

# h.Similar(['598994886'])

# h.Search(**{
#         HirajBase.RequestKeys.Search.tag:"مستلزمات شخصية",
#         HirajBase.RequestKeys.Search.cities:[
#                 "الرياض"
#             ],
#         HirajBase.RequestKeys.Search.search:"ساعة"
#     })

# h.PostContact(109876295)







