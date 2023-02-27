from time import  sleep
import json , requests , json  
from Packages import  (
    DataBase , 
    QObject,
    pyqtSignal ,
    DateOperations ,
    Generator , 
    typing
    )


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

class DataTableFlags():
    AdsData = 'AdsData'
    CommentsData = 'CommentsData'
    ContactsData = 'ContactsData'
    ProfilesData = 'ProfilesData'
    UsersData = 'UsersData'
    Leads = 'Leads'

######################################


class PostObject(object): # Completed ...
    def __init__(self,Post:dict):
        self.AdID = 0
        self.AdCreatorID = 0
        self.AdCreatorUsername = ''
        self.id = Post[ResponseKeys.Search.id] if ResponseKeys.Search.id in Post.keys() else 0
        self.authorUsername = Post[ResponseKeys.Search.authorUsername] if ResponseKeys.Search.authorUsername in Post.keys() else 'None' 
        self.authorId = Post[ResponseKeys.Search.authorId] if ResponseKeys.Search.authorId in Post.keys() else 0
        self.title = Post[ResponseKeys.Search.title] if ResponseKeys.Search.title in Post.keys() else 'None'
        self.URL = Post[ResponseKeys.Search.URL] if ResponseKeys.Search.URL in Post.keys() else 'None'
        self.city = Post[ResponseKeys.Search.city] if ResponseKeys.Search.city in Post.keys() else 'None'
        self.geoCity = Post[ResponseKeys.Search.geoCity] if ResponseKeys.Search.geoCity in Post.keys() else 'None'
        self.geoNeighborhood = Post[ResponseKeys.Search.geoNeighborhood] if ResponseKeys.Search.geoNeighborhood in Post.keys() else 'None'
        self.commentCount = Post[ResponseKeys.Search.commentCount] if ResponseKeys.Search.commentCount in Post.keys() else 0
        self.commentEnabled = Post[ResponseKeys.Search.commentEnabled]  if ResponseKeys.Search.commentEnabled in Post.keys() else False
        self.bodyTEXT = Post[ResponseKeys.Search.bodyTEXT]  if ResponseKeys.Search.bodyTEXT in Post.keys() else 'None'
        self.imagesList =  "".join([f"{x}\n" for x in Post[ResponseKeys.Search.imagesList] ]) if ResponseKeys.Search.imagesList in Post.keys() else ''
        self.tags = "".join([f"{x}\n" for x in Post[ResponseKeys.Search.tags] ]) if ResponseKeys.Search.tags in Post.keys() else ''
        self.postDate = Post[ResponseKeys.Search.postDate] if ResponseKeys.Search.postDate in Post.keys() else 0
        self.updateDate = Post[ResponseKeys.Search.updateDate] if ResponseKeys.Search.updateDate in Post.keys() else 0
        self.status = Post[ResponseKeys.Search.status] if ResponseKeys.Search.updateDate in Post.keys() else True
        self.MethodType = Post['MethodType'] if 'MethodType' in Post.keys() else 'None' 
        self.similarPostID = Post['similarPostID'] if 'similarPostID' in Post.keys() else 0
        self.Data = DataBase('Data\DataBase.db')
        self.Date = DateOperations() 
        self.DateScraping = self.Date.getCurrentDate()
        if self.Data.Search(table=DataTableFlags.AdsData,column='id',val=self.id,indexretval= 3) == None:
            self.addToDataBase()

    def __str__(self) -> str:
        return str(self.__dict__)
        
    @property
    def dictOfObject(self)->dict:
        return self.__dict__

    def addToDataBase(self):
        self.Data.addToDataAsDict(table = DataTableFlags.AdsData,**self.dictOfObject)


class AbstractHirajObject(object):
    def __init__(self,parent:PostObject,Response:dict) -> None:
        self.Response = Response
        self.parent = parent
        self.AdID = parent.id
        self.AdCreatorID = parent.authorId
        self.AdCreatorUsername = parent.authorUsername
        self.Data = DataBase('Data\DataBase.db')
        self.Date = DateOperations() 

    def __str__(self) -> str:
        return str(self.dictOfObject)
        
    @property
    def dictOfObject(self)->dict:
        return self.__dict__

    def addToDataBase(self,table:DataTableFlags):
        self.DateScraping = self.Date.getCurrentDate(DateOperations.TimeFlags.Epoch)
        self.Data.addToDataAsDict(
            table = table,
            **self.dictOfObject
        )
        

class PostContactObject(AbstractHirajObject): # Completed ...
    def __init__(self, parent: PostObject, Response: dict) -> None:
        super().__init__(parent, Response)
        self.contactText = Response['data']['postContact']['contactText']
        self.contactMobile = Response['data']['postContact']['contactMobile']
        if self.Data.Search(table=DataTableFlags.ContactsData,column='contactMobile',val=self.contactMobile,indexretval= 4) == None:
            self.addToDataBase()

    def addToDataBase(self):
        return super().addToDataBase(DataTableFlags.ContactsData)


class ProfileObject(AbstractHirajObject): # Completed
    def __init__(self, parent: PostObject, Response: dict) -> None:
        super().__init__(parent, Response)
        # print(Response)
        if Response['data']['profile'] != None :
            self.id = Response['data']['profile']['id']
            self.handler = Response['data']['profile'][ResponseKeys.Profile.handler]
            self.type = Response['data']['profile'][ResponseKeys.Profile.type]
            self.description = Response['data']['profile'][ResponseKeys.Profile.description]
            self.contacts = Response['data']['profile'][ResponseKeys.Profile.contacts]
            if self.Data.Search(table=DataTableFlags.ProfilesData,column='id',val=self.id,indexretval=3) == None:
                self.addToDataBase()
        else:
            self.id = parent.id #Response['data']['profile']['id']
            self.handler = parent.authorUsername  #Response['data']['profile'][ResponseKeys.Profile.handler]
            self.type = None #Response['data']['profile'][ResponseKeys.Profile.type]
            self.description = None #Response['data']['profile'][ResponseKeys.Profile.description]
            self.contacts = None #Response['data']['profile'][ResponseKeys.Profile.contacts]
            if self.Data.Search(table=DataTableFlags.ProfilesData,column='id',val=self.id,indexretval=3) == None:
                self.addToDataBase()

    def addToDataBase(self):
        return super().addToDataBase(DataTableFlags.ProfilesData)
        

class PostsResponseObject(AbstractHirajObject):# Completed

    def __init__(self,response:dict) -> None:
        self.Response = response
        self.hasNextPage = False
        if 'search' in response['data'].keys() :
            self.Type = PayloadQueryTypeFlags.Search #'Search'
            self.hasNextPage = response['data']['search']['pageInfo']['hasNextPage']

        elif 'similarPosts' in response['data'].keys() :
            self.Type = PayloadQueryTypeFlags.SimilarPosts
            # self.hasNextPage = False

        elif 'posts' in response['data'].keys() :
            self.Type = PayloadQueryTypeFlags.FetchAds
            self.hasNextPage = response['data']['posts']['pageInfo']['hasNextPage']
        
        elif 'postContact' in response['data'].keys():
            self.Type = PayloadQueryTypeFlags.PostContact
            # self.hasNextPage = False
        
        elif 'comments' in response['data'].keys():
            self.Type = PayloadQueryTypeFlags.Comments
            self.hasNextPage =  response['data']['comments']['pageInfo']['hasNextPage']

        elif 'profile' in response['data'].keys():
            self.Type = PayloadQueryTypeFlags.Profile
            # self.hasNextPage =  False

        elif 'user' in response['data'].keys():
            self.Type = PayloadQueryTypeFlags.User
            # self.hasNextPage =  False

    @property
    def Posts(self)-> typing.List[PostObject]:
        Posts = []
        if self.Type == PayloadQueryTypeFlags.Search :
            for Ad in self.Response["data"]["search"]["items"] :
                Post = PostObject(Ad)
                Posts.append(Post)

        elif self.Type == PayloadQueryTypeFlags.SimilarPosts :
            for Ad in self.Response["data"]['similarPosts']['groupTags'][0]['posts']['items'] :
                Post = PostObject(Ad)
                Posts.append(Post)

        elif self.Type == PayloadQueryTypeFlags.FetchAds :
            for Ad in self.Response['data']['posts']['items'] :
                Post = PostObject(Ad)
                Posts.append(Post)

        return Posts

    def addToDataBase(self):
        pass


class CommentObject(AbstractHirajObject):
    def __init__(self, parent: PostObject, Response: dict) -> None:
        super().__init__(parent, Response)
        self.id = Response['id']
        self.authorUsername = Response['authorUsername']
        self.authorId = Response['authorId']
        self.authorLevel = Response['authorLevel']
        self.body = Response['body']
        self.isNewUser = Response['isNewUser']
        self.status = Response['status']
        self.deleteReason = Response['deleteReason']
        self.seqId = Response['seqId']
        self.date = Response['date']
        if self.Data.Search(table=DataTableFlags.CommentsData,column='id',val=self.id,indexretval=3) == None:
            self.addToDataBase()
    
    def addToDataBase(self):
        return super().addToDataBase(DataTableFlags.CommentsData)


class CommentsObject(AbstractHirajObject):
    def __init__(self, parent: PostObject, Response: dict) -> None:
        super().__init__(parent,Response)
        self.hasNextPage = Response['data']['comments']['pageInfo']['hasNextPage']

    @property
    def Comments(self) -> typing.List[CommentObject]:
        Comments = []
        for comment in self.Response['data']['comments']['items']:
            Comments.append(CommentObject(self.parent,comment))
        return Comments

    @property
    def CommenterNames(self)->typing.List[str]:
        return [comment.authorUsername for comment in self.Comments]


    def addToDataBase(self):
        pass


class UserObject(AbstractHirajObject):
    def __init__(self, parent: PostObject, Response: dict) -> None:
        super().__init__(parent, Response)
        self.id = Response['data']['user']['id']
        self.username = Response['data']['user']['username']
        self.registrationDate = Response['data']['user']['registrationDate']
        self.mobile = Response['data']['user']['mobile']
        self.isMember = Response['data']['user']['isMember']
        self.isAdmin = Response['data']['user']['isAdmin']
        self.isBlocked = Response['data']['user']['isBlocked']
        self.isBlocked = Response['data']['user']['isBlocked']
        self.lastSeen = Response['data']['user']['lastSeen']
        self.lastSeenString =  str(self.Date.translateTimeFromStampToDate(self.lastSeen)) if isinstance(self.lastSeen , int) else "last seen Not Found" 
        self.countFollowers = Response['data']['user']['countFollowers']
        if self.Data.Search(table=DataTableFlags.UsersData,column='id',val=self.id,indexretval=3) == None:
            self.addToDataBase()

    def addToDataBase(self):
        return super().addToDataBase(DataTableFlags.UsersData)
        

class HirajBase(QObject):
    msg = pyqtSignal(str)
    LeadsSignal = pyqtSignal(dict)
    AdIDSignal = pyqtSignal(int)
    UserIDSignal = pyqtSignal(int)
    status = pyqtSignal(str)

    class Flags():
        Random = 'Random'
        Normal = 'Normal'
        Yes = 'Yes'
        No = 'No'

    class URLs():
        First = 'https://graphql.haraj.com.sa/' # ALL
        Secound = 'https://matjar.haraj.com.sa/graphql'  # Profile 

    def __init__(
        self 
        ) -> None:

        self.Data = DataBase('Data\DataBase.db')
        self.Date = DateOperations() 
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
        url = self.URLs.Secound if RequestType == PayloadQueryTypeFlags.Profile else self.URLs.First
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

    def Search(self,**kwargs) -> PostsResponseObject:
        self.status.emit(f"Sending Search Request ")
        return PostsResponseObject(self.sendRequest(PayloadQueryTypeFlags.Search,**kwargs)) 
         
    def FetchAds(self,**kwargs)-> PostsResponseObject:
        self.status.emit(f"Sending FetchAds Request ")
        return PostsResponseObject(self.sendRequest(PayloadQueryTypeFlags.FetchAds,**kwargs))

    def Profile(self,parent:PostObject) -> ProfileObject:
        self.status.emit(f"Sending Profile Request ")
        return ProfileObject(parent,self.sendRequest(PayloadQueryTypeFlags.Profile,**{RequestKeys.Profile.id : parent.id}))
    
    def Comments(self,parent:PostObject)-> CommentsObject:
        self.status.emit(f"Sending Comments Request ")
        return CommentsObject(parent,self.sendRequest(PayloadQueryTypeFlags.Comments,**{RequestKeys.Comments.postId : parent.id}))

    def PostContact(self,parent:PostObject)-> PostContactObject:
        self.status.emit(f"Sending PostContact Request ")
        return PostContactObject(
            parent ,
            self.sendRequest(
                RequestType = PayloadQueryTypeFlags.PostContact ,
                UserAgent = self.Flags.Random ,
                ClientID = self.Flags.Random ,
                **{RequestKeys.postContact.postId:parent.id})
        )
                
    def SimilarPosts(self,PostIDSimilar:int)-> PostsResponseObject:
        self.status.emit(f"Sending SimilarPosts Request ")
        return PostsResponseObject(self.sendRequest(PayloadQueryTypeFlags.SimilarPosts,**{RequestKeys.SimilarPosts.id:PostIDSimilar}))

    def User(self,parent:PostObject)->UserObject: 
        self.status.emit(f"Sending User Request ")
        return UserObject(parent,self.sendRequest(PayloadQueryTypeFlags.User,**{RequestKeys.User.Username:parent.authorUsername}))


class LeadObject(AbstractHirajObject):
    def __init__(self,parent:PostObject,BaseClass:HirajBase) -> None:
        super().__init__(parent,Response={})
        self.UserName = parent.authorUsername
        self.Title = parent.title
        self.PhoneNumber = BaseClass.PostContact(parent).contactMobile
        self.LastSeen = BaseClass.User(parent).lastSeenString
        # print("\nlead search->",self.Data.Search(table=DataTableFlags.Leads,column='PhoneNumber',val=self.PhoneNumber,indexretval=1))
        self.new = False
        if self.Data.Search(table=DataTableFlags.Leads,column='PhoneNumber',val=self.PhoneNumber,indexretval=1) == None and self.PhoneNumber != '':
            self.new = True
            self.addToDataBase()
            # print("Lead Added to database")

    def addToDataBase(self):
        return super().addToDataBase(DataTableFlags.Leads)
