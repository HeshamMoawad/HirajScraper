from time import  sleep
from datetime import datetime
import json
from MyPyQt5 import  (
    Validation , 
    DataBase , 
    QObject,
    pyqtSignal ,
    DateOperations
    )


class Hiraj(QObject):
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

    class PayloadQueryFlags():
        FetchAds = {
        "query": "\n    query FetchAds($isRe: Boolean = true, $id: [Int] = null, $city: String = null, $cities: [String], $authorUsername: String = null, $page: Int = null, $limit: Int = null, $afterPostDate: Int = null, $afterUpdateDate: Int = null, $beforeUpdateDate: Int = null, $beforePostDate: Int = null, $tag: String = null, $near: String = null, $onlyWithImage: Boolean = null, $orderMainByPostId: Boolean = null, $notTag: String = null) {\n  posts(\n    id: $id\n    city: $city\n    cities: $cities\n    authorUsername: $authorUsername\n    page: $page\n    limit: $limit\n    afterPostDate: $afterPostDate\n    afterUpdateDate: $afterUpdateDate\n    beforeUpdateDate: $beforeUpdateDate\n    beforePostDate: $beforePostDate\n    tag: $tag\n    near: $near\n    onlyWithImage: $onlyWithImage\n    orderMainByPostId: $orderMainByPostId\n    notTag: $notTag\n  ) {\n    items {\n      id\n      title\n      postDate\n      updateDate\n      authorUsername\n      authorId\n      URL\n      bodyTEXT\n      bodyHTML\n      thumbURL\n      hasImage\n      city\n      geoCity\n      geoNeighborhood\n      geoHash\n      tags\n      imagesList\n      commentEnabled\n      commentCount\n      upRank\n      downRank\n      status\n      postType\n      price {\n        formattedPrice\n      }\n      realEstateInfo @include(if: $isRe) {\n        ...realEstateOptions\n      }\n    }\n    pageInfo {\n      hasNextPage\n    }\n  }\n}\n    \n    fragment realEstateOptions on reInfo {\n  re_AdvertiserType\n  re_Direction\n  re_StreetType\n  re_AccommType\n  re_IsKitchenIncluded\n  re_IsFurnished\n  re_IsDriverRoomAvilable\n  re_IsMaidRoomAvilable\n  re_IsFireRoomAvilable\n  re_IsOutsideRoomAvilable\n  re_IsCarGateAvilable\n  re_IsElevatorAvilable\n  re_IsParkingAvilable\n  re_IsCellarIncludedAvilable\n  re_IsGardenAvilable\n  re_IsACIncludedAvilable\n  re_IsPoolAvilable\n  re_IsVolleyBallAvilable\n  re_IsFootBallAvilable\n  re_IsKidsGamesAvilable\n  re_IsStairInsideAvilable\n  re_IsYardAvilable\n  re_IsBooked\n  re_Area\n  re_PropertyAge\n  re_StreetWide\n  re_RoomCount\n  re_LivingRoomCount\n  re_WCCount\n  re_ApartmentCount\n  re_CheckInDate\n  re_CheckOutDate\n  re_VillaCount\n  re_PlanNum\n  re_LandNum\n  re_MachineCount\n  re_PalmCount\n  re_MeterPrice\n  re_FloorNum\n  re_REGA_Advertiser_registration_number\n  re_REGA_Authorization_number\n  re_VillaType\n  re_IsOutdoorSessionsAvailable\n  re_IsLivingRoomAvailable\n  re_IsTransformerAvailable\n  re_IsWCAvailable\n  re_IsStageAvailable\n  re_IsStorehouseAvailable\n  re_IsWaterAvailable\n  re_IsProtectoratesAvailable\n  re_IsElectricityAvailable\n  re_IsPrivateHallAvailable\n  re_IsPrivateEntranceAvailable\n  re_IsWorkersHouseAvailable\n  re_IsTentHouseAvailable\n  re_IsFoodHallAvailable\n  re_IsTwoDepartment\n  re_IsWaterTankAvailable\n  re_IsPrivateHouseAvailable\n  re_IsBridalDepartmentAvailable\n  re_IsPlowAvailable\n  re_IsGymAvailable\n  re_IsWaterSprinklerAvailable\n  re_TentCount\n  re_WellsCount\n  re_HallsCount\n  re_FloorsCount\n  re_TentHouseCount\n  re_SessionsCount\n  re_ShopsCount\n  re_SupportDailyRentSystem\n  re_SupportMonthlyRentSystem\n  re_SupportYearlyRentSystem\n}\n    ",
        "variables": {
            "isRe": True,
            "city": None,
            "authorUsername": None,
            "page": None,
            "limi": None,
            "tag": None,
            "id": [],
            "orderMainByPostId": False
        }
    }
        comments = {
        "query": "query comments($postId: Int!, $page: Int, $token: String) {\n    \n  comments(postId: $postId, page: $page, token: $token)\n  { \n    items {\n        id\n        authorUsername\n        authorId\n        authorLevel\n        body\n        isNewUser\n        status\n        deleteReason\n        seqId\n        date\n    }\n    pageInfo {\n        hasNextPage\n    }\n }\n  \n  }",
        "variables": {
            "postId": 109666696,
            "page": 1,
            "token": ""
        }
    }
        postContact = {
        "query": "query postContact($postId: Int!, $isManualRequest: Boolean) {\n    \n  postContact(postId: $postId, isManualRequest: $isManualRequest)\n  { \n    contactText\n    contactMobile\n }\n  \n  }",
        "variables": {
            "postId": 109666696,
            "isManualRequest": True
        }
    }
        similarPosts = {
        "query": "query similarPosts($id: Int!) {\n    \n  similarPosts(id: $id)\n  { \n    id\n    groupTags {\n      tag\n      city\n      posts {\n        items {\n          id\n          status\n          authorUsername\n          title\n          city\n          postDate\n          updateDate\n          hasImage\n          thumbURL\n          imagesList\n          bodyHTML\n          bodyTEXT\n          authorId\n          tags\n          upRank\n          downRank\n          city\n          geoCity\n          geoNeighborhood\n          geoHash\n          commentEnabled\n          commentStatus\n        }\n      }\n    }\n }\n  \n  }",
        "variables": {
            "id": 109666665
        }
    }
        Search = {
        "query": "\n    query Search($id: [Int], $cities: [String], $search: String!, $city: String, $authorUsername: String, $page: Int, $limit: Int, $afterPostDate: Int, $afterUpdateDate: Int, $tag: String, $tags: [String], $carExtraInfo: CarExtraInfo, $near: String, $onlyWithImage: Boolean, $duringDate: String, $userLocation: GeoPoint, $notTag: String, $hideShowRooms: Boolean, $orderByPostId: Boolean) {\n  search(\n    id: $id\n    search: $search\n    city: $city\n    cities: $cities\n    authorUsername: $authorUsername\n    page: $page\n    limit: $limit\n    afterPostDate: $afterPostDate\n    afterUpdateDate: $afterUpdateDate\n    tag: $tag\n    tags: $tags\n    CarExtraInfo: $carExtraInfo\n    near: $near\n    onlyWithImage: $onlyWithImage\n    userLocation: $userLocation\n    duringDate: $duringDate\n    notTag: $notTag\n    hideShowRooms: $hideShowRooms\n    orderByPostId: $orderByPostId\n  ) {\n    items {\n      id\n      authorUsername\n      authorId\n      hasImage\n      title\n      URL\n      icon\n      city\n      geoCity\n      geoNeighborhood\n      geoHash\n      commentCount\n      commentEnabled\n      thumbURL\n      bodyHTML\n      bodyTEXT\n      imagesList\n      tags\n      postDate\n      updateDate\n      status\n      upRank\n      downRank\n    }\n    pageInfo {\n      hasNextPage\n    }\n  }\n}\n    ",
        "variables": {
            "tag": "",
            "correctedWords": [],
            "search": "",
            "orderByPostId": False,
            "page": 1 ,
            "cities": [] ,
        }
    }
        Profile =  {
        "query": "query profile($id: ID!) {\n    \n  profile(id: $id)\n  { \n    id\n    handler\n    type\n    description\n    pages {\n      id\n      title\n      order\n      content\n    }\n    locations {\n        id\n        value\n        description\n    }\n    contacts {\n        id\n        description\n        info\n        type\n    }\n    verifications {\n        id\n        type\n        status\n        data\n    }\n    updatedAt \n }\n  \n  }",
            "variables": {
                "id": 2836074
        }
    }
        User = {
        "query": "query user($username: String) {\n    \n  user(username: $username)\n  { \n\t\tid\n\t\tusername\n\t\tregistrationDate\n\t\tmobile\n\t\tdiscount\n\t\tisMember\n\t\tisAdmin\n\t\tisBlocked\n\t\tdidPay\n\t\tlastSeen\n\t\tcountFollowers\n\t\tratingSummery {\n        upRank\n        downRank\n        rateAverage\n\t\t}\n\t\tbadges {\n\t\t    badge\n\t\t}\n }\n  \n  }",
        "variables": {
            "username": "شركة دائرة التشييدللمقاولات"
        }
    }

    class PayloadQueryTypeFlags():
        FetchAds = 'FetchAds'
        comments = 'comments'
        postContact = 'postContact'
        similarPosts = 'similarPosts'
        Search = 'Search'

    class RequestKeys():

        class Search():
            tag = 'tag' # Str
            cities = 'cities' # List
            search = 'search' # Keyword
        
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


    def __init__(self) -> None:
        self.Data = DataBase('Data\DataBase.db')
        self.Date = DateOperations() 
        self.AdID = 0
        self.AdCreatorID = 0
        self.AdCreatorUsername = ''

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
        self.Data.add_to_db(
            table = table,
            **response
        )
        
        

    def resolveSearchResponse(self,response) -> list: #  Done #####
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

        return resultIDs


    def resolveCommentsResponse(self,response)-> list: # Done  #######
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
        return commenterIDs


    def resolvePostContactResponse(self,response)-> str: # Done #####
        response = response['data']['postContact']
        self.addToDataBase(
            table = self.DataTableFlags.ContactsData ,
            response = response
        )
        self.LeadsSignal.emit({'UserName':self.AdCreatorUsername ,'PhoneNumber':response[self.ResponseKeys.postContact.contactMobile]})
        return response[self.ResponseKeys.postContact.contactMobile]

        
        

    def resolveSimilarPostsResponse(self,response): # Done
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
        


        
    def resolveFetchAdsResponse(self,response):
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


    def resolveProfileResponse(self,response):
        response = response['data']['profile']
        response['contacts'] = [f"{x['info']}\n" for x in response['contacts'] ]
        self.addToDataBase(
            table = self.DataTableFlags.ProfilesData ,
            response = response
        )
        


