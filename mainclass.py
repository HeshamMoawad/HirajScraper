from time import  sleep
from datetime import datetime
import json , requests , json
from ProxyFilterClass import ProxyFilterAPI
from MyPyQt5 import  (
    Validation , 
    DataBase , 
    QObject,
    pyqtSignal ,
    DateOperations ,
    MyMessageBox 
    )


class Hiraj(QObject):
    msg = MyMessageBox()
    LeadsSignal = pyqtSignal(dict)
    AdIDSignal = pyqtSignal(int)
    UserIDSignal = pyqtSignal(int)

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
        self ,
        Proxy:ProxyFilterAPI.ProxyFlags=ProxyFilterAPI.ProxyFlags.NoProxy ,

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
        }
        self.Payloads = json.load(open('Payloads\Payload.json','r'))
        self.ProxyAPI = ProxyFilterAPI()
        self.ProxyFlag = Proxy
        super().__init__()

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
        self.Data.add_to_db(
            table = table,
            **response
        )
        
        

    def resolveSearchResponse(self,response:dict) -> dict: #  Done #####
        resultIDs = []
        for Ad in response["data"]["search"]["items"] :
            id = Ad[self.ResponseKeys.Search.id]
            if not self.Data.exist(table = "AdsData" ,column='id' ,val = id ):
                Ad['MethodType'] = 'Search'
                Ad['similarPostID'] = 0
                self.addToDataBase(
                    table = self.DataTableFlags.AdsData ,
                    response = Ad
                    )
                self.AdIDSignal.emit(int(id))
                resultIDs.append(id)
        HasNextPage = response["data"]["search"]["pageInfo"]['hasNextPage']
        return {"Result": resultIDs ,"HasNextPage":HasNextPage}



    def resolveCommentsResponse(self,response:dict)-> dict: # Done  #######
        commenterIDs = []
        for comment in response["data"]['comments']['items'] :
            id = comment['id']
            if not self.Data.exist(table = "CommentsData" ,column='id' ,val = id ):
                self.addToDataBase(
                    table = self.DataTableFlags.CommentsData ,
                    response = comment
                )
                self.UserIDSignal.emit(int(comment['authorId']))
                commenterIDs.append(comment['authorId'])
        HasNextPage = response["data"]['comments']['pageInfo']['hasNextPage']
        return {"Result": commenterIDs ,"HasNextPage":HasNextPage}


    def resolvePostContactResponse(self,response:dict)-> str: # Done #####
        response = response['data']['postContact']
        self.addToDataBase(
            table = self.DataTableFlags.ContactsData ,
            response = response
        )
        self.LeadsSignal.emit({'UserName':self.AdCreatorUsername ,'PhoneNumber':response[self.ResponseKeys.postContact.contactMobile]})
        return response[self.ResponseKeys.postContact.contactMobile]

        
        

    def resolveSimilarPostsResponse(self,response:dict)-> list : # Done
        resultIDs = []
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
                resultIDs.append(id)
        return resultIDs
        


        
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
                resultIDs.append(id)
        return resultIDs


    def resolveProfileResponse(self,response:dict):
        response = response['data']['profile']
        response['contacts'] = "".join([f"{x['info']}\n" for x in response['contacts']])
        self.addToDataBase(
            table = self.DataTableFlags.ProfilesData ,
            response = response
        )
        


    def sendRequest(
        self,
        RequestType:PayloadQueryTypeFlags,
        Proxy:ProxyFilterAPI.ProxyFlags = ProxyFilterAPI.ProxyFlags.NoProxy,
        **kwargs
        ) -> dict:

        url = self.URLs.Secound if RequestType == self.PayloadQueryTypeFlags.Profile else self.URLs.First
        Payload = self.Payloads[RequestType]
        for key,value in kwargs.items():
            Payload['variables'][key] = value
        response = requests.post(
            url = url ,
            headers = self.header ,
            json = Payload ,
            proxies = self.ProxyAPI.getRandomProxyWithTimeOut(30) if self.ProxyFlag == self.ProxyAPI.ProxyFlags.RandomProxy else None ,
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





h= Hiraj()
print(h.sendRequest(h.PayloadQueryTypeFlags.FetchAds))






