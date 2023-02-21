from time import  sleep
import json , requests , json  
from Packages import  (
    DataBase , 
    QObject,
    pyqtSignal ,
    DateOperations ,
    Generator , 
    pandas
    )



class HirajBase(QObject):
    msg = pyqtSignal(str)
    LeadsSignal = pyqtSignal(dict)
    AdIDSignal = pyqtSignal(int)
    UserIDSignal = pyqtSignal(int)

    class Flags():
        Random = 'Random'
        Normal = 'Normal'
        Yes = 'Yes'
        No = 'No'

    class DataTableFlags():
        AdsData = 'AdsData'
        CommentsData = 'CommentsData'
        ContactsData = 'ContactsData'
        ProfilesData = 'ProfilesData'
        UsersData = 'UsersData'

    class URLs():
        First = 'https://graphql.haraj.com.sa/' # ALL
        Secound = 'https://matjar.haraj.com.sa/graphql'  # Profile 

    class PayloadQueryTypeFlags():
        FetchAds = 'FetchAds'
        Comments = 'comments'
        PostContact = 'postContact'
        SimilarPosts = 'similarPosts'
        Search = 'Search'
        Profile = 'Profile'
        User = 'user' 

    class RequestKeys():

        class Search():
            tag = 'tag' # Str
            cities = 'cities' # List
            search = 'search' # Keyword
            page = 'page' # Page

        class Profile():
            id = 'id'
        
        class SimilarPosts():
            id = 'id'
        
        class Comments():
            postId = 'postId'
            page = 'page'

        class postContact():
            postId = 'postId'
            isManualRequest = 'isManualRequest'

        class User():
            Username = 'username'

        class FetchAds():
            city = 'city' # Str
            authorUsername = 'authorUsername'
            tag = 'tag'
            PostID = 'id' # List
            page = 'page' 

    class ResponseKeys():
        class AdInfo():
            id = 'id' # Int
            authorUsername = 'authorUsername' # Str
            authorId = 'authorId'  # Int
            title = 'title' # Str
            URL = 'URL' # Str
            city = 'city' # Str
            geoCity = 'geoCity' # Str
            geoNeighborhood = 'geoNeighborhood' # Str
            commentCount = 'commentCount' # Int
            commentEnabled = 'commentEnabled' # Bool
            bodyTEXT = 'bodyTEXT' # Str
            imagesList = 'imagesList' # List
            tags = 'tags' # List
            postDate = 'postDate'  # Int
            updateDate = 'updateDate' # Int
            status = 'status' # Bool

        class Search(AdInfo):
            ...

        class FetchAds(AdInfo):
            ...

        class Comments():
            id = "id"
            authorUsername = "authorUsername"
            authorId = "authorId"
            body = "body"
            isNewUser = "isNewUser"
            status = "status"
            deleteReason = "deleteReason"
            date = "date"

        class postContact():
            contactText = 'contactText'
            contactMobile = 'contactMobile'

        class similarPosts(AdInfo):
            ...

        class Profile():
            id = "id"
            handler = "handler"
            type = "type"
            description = "description"
            contacts = 'contacts'
            class Contacts():
                info= "info" # PhoneNumber

        class  User():
            id = "id"
            username = "username"
            registrationDate = "registrationDate"
            mobile = "mobile"
            discount = "discount"
            isMember = "isMember"
            isAdmin = "isAdmin"
            isBlocked = "isBlocked"
            lastSeen= "lastSeen"
            countFollowers= "countFollowers"


    def __init__(
        self 
        ) -> None:

        self.Data = DataBase('Data\DataBase.db')
        self.Date = DateOperations() 
        self.AdID = 0
        self.AdCreatorID = 0
        self.AdCreatorUsername = ''
        self.header = {
            'Content-Type': 'application/json' ,
            'Accept':'*/*' ,
            'Accept-Encoding' : 'gzip, deflate, br' ,
            'Connection' : 'keep-alive',
            'accept-language' : 'en-US,en;q=0.9',
            'origin' : 'https://haraj.com.sa' ,
            'referer' : 'https://haraj.com.sa/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36' # PostmanRuntime/7.31.0
        }
        self.Payloads = json.load(open('Payloads\Payload.json','r'))
        super().__init__()
        self.generator = Generator()


    def setCreator(self,AdID:int,AdCreatorID:int,AdCreatorUsername:str):
        self.AdID = AdID
        self.AdCreatorID = AdCreatorID
        self.AdCreatorUsername = AdCreatorUsername

    def addToDataBase(self,table:DataTableFlags,response:dict):
        response['AdID'] = self.AdID
        response['AdCreatorID'] = self.AdCreatorID
        response['AdCreatorUsername'] = self.AdCreatorUsername
        response['DateScraping'] = self.Date.getCurrentDate()
        if table == self.DataTableFlags.AdsData:
            response[self.ResponseKeys.AdInfo.imagesList] = "".join([f"{x}\n" for x in response[self.ResponseKeys.AdInfo.imagesList] ])
            response[self.ResponseKeys.AdInfo.tags] = "".join([f"{x}\n" for x in response[self.ResponseKeys.AdInfo.tags] ])
        self.Data.addToDataAsDict(
            table = table,
            **response
        )
        
    def resolveSearchResponse(self,response:dict) -> dict: #  Done #####
        resultIDs = []
        for Ad in response["data"]["search"]["items"] :
            id = Ad[self.ResponseKeys.Search.id]
            if not self.Data.exist(table = self.DataTableFlags.AdsData ,column = 'AdID'  ,val = id ):
                Ad['MethodType'] = 'Search'
                Ad['similarPostID'] = 0
                self.addToDataBase(
                    table = self.DataTableFlags.AdsData ,
                    response = Ad
                    )
                self.AdIDSignal.emit(int(id))
                resultIDs.append(Ad)
        HasNextPage = response["data"]["search"]["pageInfo"]['hasNextPage']
        return {"Result": resultIDs ,"HasNextPage":HasNextPage}

    def resolveCommentsResponse(self,response:dict)-> dict: # Done  #######
        commenterNames = []
        for comment in response["data"]['comments']['items'] :
            id = comment['id']
            if not self.Data.exist(table = "CommentsData" ,column='id' ,val = id ):
                self.addToDataBase(
                    table = self.DataTableFlags.CommentsData ,
                    response = comment
                )
                self.UserIDSignal.emit(int(comment['authorId']))
                commenterNames.append(comment[self.ResponseKeys.Comments.authorUsername])
        HasNextPage = response["data"]['comments']['pageInfo']['hasNextPage']
        return {"Result": commenterNames ,"HasNextPage":HasNextPage}

    def resolvePostContactResponse(self,response:dict)-> str: # Done #####
        response = response['data']['postContact']
        self.addToDataBase(
            table = self.DataTableFlags.ContactsData ,
            response = response
        )
        self.LeadsSignal.emit({'UserName':self.AdCreatorUsername ,'PhoneNumber':response[self.ResponseKeys.postContact.contactMobile]})
        return response[self.ResponseKeys.postContact.contactMobile]

    def resolveSimilarPostsResponse(self,response:dict)-> list : # Done
        result = []
        similarPostID = response["data"]['similarPosts']['id']
        for Ad in response["data"]['similarPosts']['groupTags'][0]['posts']['items'] :
            id = Ad['id']
            if not self.Data.exist(table = self.DataTableFlags.AdsData ,column= 'AdID' ,val = id ):
                Ad['MethodType'] = 'SimilarPosts'
                Ad['similarPostID'] = similarPostID
                self.addToDataBase(
                    table = self.DataTableFlags.AdsData ,
                    response = Ad
                )
                self.AdIDSignal.emit(int(id))
                result.append(Ad)
        return result
        
    def resolveFetchAdsResponse(self,response:dict)->dict:
        resultIDs = []
        for Ad in response['data']['posts']['items'] :
            id = Ad['id']
            if not self.Data.exist(table=self.DataTableFlags.AdsData , column = 'AdID',val = id) :
                Ad['MethodType'] = 'FetchAds'
                Ad['similarPostID'] = 0
                self.addToDataBase(
                    table = self.DataTableFlags.AdsData,
                    response = Ad
                )
                resultIDs.append(Ad)
        HasNextPage = response['data']['posts']['pageInfo']['hasNextPage']
        return {"Result": resultIDs ,"HasNextPage":HasNextPage}

    def resolveProfileResponse(self,response:dict):
        response = response['data']['profile']
        print(response)
        if response != None:
            response['contacts'] = "".join([f"{x['info']}\n" for x in response['contacts']])
            self.addToDataBase(
                table = self.DataTableFlags.ProfilesData ,
                response = response
            )
        
    def resolveUserResponse(self,response:dict)-> int:
        response = response['data']['user']
        self.addToDataBase(
            table = self.DataTableFlags.UsersData ,
            response = response
        )
        return response['lastSeen']

    def getHeaders(self,UserAgentType :Flags = Flags.Normal):
        header = self.header
        if UserAgentType == self.Flags.Random :
            header['User-Agent'] = self.generator.getRandomUserAgent()
        else :
            header = self.header
        return header

    def getClientID(self,ClientIDType :Flags = Flags.Normal):
        if ClientIDType == self.Flags.Random:
            clientID = {'clientId': self.generator.generateClientID()}
        else:
            clientID = {}
        return clientID

    def sendRequest(
        self,
        RequestType:PayloadQueryTypeFlags,
        UserAgent:Flags = Flags.Normal,
        ClientID :Flags = Flags.Normal ,
        **kwargs
        ) -> dict:

        url = self.URLs.Secound if RequestType == self.PayloadQueryTypeFlags.Profile else self.URLs.First
        Payload = self.Payloads[RequestType]
        for key,value in kwargs.items():
            Payload['variables'][key] = value
        response = requests.post(
            url = url ,
            headers = self.getHeaders(UserAgent) ,
            json = Payload ,
            params = self.getClientID(ClientID)
        )
        return  response.json()

    def Search(self,**kwargs):
        Response = self.sendRequest(self.PayloadQueryTypeFlags.Search,**kwargs)
        return self.resolveSearchResponse(Response)
         
    def FetchAds(self,**kwargs):
        Response = self.sendRequest(self.PayloadQueryTypeFlags.FetchAds,**kwargs)
        return self.resolveSearchResponse(Response)

    def Profile(self,UserID:int):
        Response = self.sendRequest(
            self.PayloadQueryTypeFlags.Profile,
            **{self.RequestKeys.Profile.id : UserID} ,
            )
        self.resolveProfileResponse(Response)
    
    def Comments(self,PostID:int):
        Response = self.sendRequest(
            self.PayloadQueryTypeFlags.Comments,
            **{self.RequestKeys.Comments.postId : PostID}
        )
        return self.resolveCommentsResponse(Response)

    def PostContact(self,PostID:int):
        Response = self.sendRequest(
            RequestType = self.PayloadQueryTypeFlags.PostContact ,
            UserAgent = self.Flags.Random ,
            ClientID = self.Flags.Random ,
            **{self.RequestKeys.postContact.postId:PostID}
        )
        return self.resolvePostContactResponse(Response)

    def SimilarPosts(self,PostIDSimilar:int):
        Response = self.sendRequest(
            RequestType=self.PayloadQueryTypeFlags.SimilarPosts,
            **{self.RequestKeys.SimilarPosts.id:PostIDSimilar}
            )
        return self.resolveSimilarPostsResponse(Response)

    def User(self,UserName:str): 
        Response = self.sendRequest(
            RequestType = self.PayloadQueryTypeFlags.User ,
            **{self.RequestKeys.User.Username:UserName}
        )
        return self.resolveUserResponse(Response)



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
        

    def Search(self,comments:HirajBase.Flags = HirajBase.Flags.No,**kwargs):
        AdsData = self.HirajBase.Search(**kwargs)
        self.TranslateAdsInfo(ads=AdsData['Result'],breakwhenphone=False,comments=comments)
            

    def Comments(self,PostID:int):
        commenterNames = self.HirajBase.Comments(PostID)['Result']
        for name in commenterNames:
            ads = self.HirajBase.FetchAds(
                **{self.HirajBase.RequestKeys.FetchAds.authorUsername:name}
            )['Result']
            self.TranslateAdsInfo(ads=ads,breakwhenphone=True)


    def TranslateAdsInfo(self, ads ,breakwhenphone:bool = False , comments:HirajBase.Flags = HirajBase.Flags.No):
        for Ad in ads:
            Lead = {}
            self.HirajBase.setCreator(
            AdID = Ad[HirajBase.ResponseKeys.Search.id] ,
            AdCreatorID = Ad[HirajBase.ResponseKeys.Search.authorId] ,
            AdCreatorUsername = Ad[HirajBase.ResponseKeys.Search.authorUsername]
        )
            self.HirajBase.Profile(Ad[HirajBase.ResponseKeys.Search.authorId])
            Lead['UserName'] = Ad[HirajBase.ResponseKeys.Search.authorUsername]
            Lead['Title'] = Ad[self.HirajBase.ResponseKeys.FetchAds.title]
            Lead['PhoneNumber'] = self.HirajBase.PostContact(Ad[self.HirajBase.ResponseKeys.FetchAds.id])
            Lead['LastSeen'] = str(self.HirajBase.Date.translateTimeFromStampToDate(stamp = float(self.HirajBase.User(Ad[HirajBase.ResponseKeys.Search.authorUsername]))))
            if Lead['PhoneNumber'] != '' :
                self.LeadSignal.emit(Lead)
                print(Lead)
                if breakwhenphone :
                    break
            if comments == HirajBase.Flags.Yes :
                self.Comments(Ad[HirajBase.ResponseKeys.Search.id])

    def Similar(self,numbersList:list ,comments:HirajBase.Flags = HirajBase.Flags.No):
        maindf = self.HirajBase.Data.getTabelIntoDataFrame('ContactsData')
        dflist = []
        print(maindf)
        idslist = [self.HirajBase.Data.Search('ContactsData','contactMobile',number,0) for number in numbersList ]
        for id in idslist:
            if id != None :
                ads = self.HirajBase.SimilarPosts(id)
                self.TranslateAdsInfo(ads,comments,breakwhenphone=False)
            
        



# h = HirajSlots()

# h.Similar(['598994886'])

# h.Search(**{
#         HirajBase.RequestKeys.Search.tag:"مستلزمات شخصية",
#         HirajBase.RequestKeys.Search.cities:[
#                 "الرياض"
#             ],
#         HirajBase.RequestKeys.Search.search:"ساعة"
#     })


# h = HirajBase(Proxy=ProxyFilterAPI.ProxyFlags.NoProxy)

# h.PostContact(109876295)






