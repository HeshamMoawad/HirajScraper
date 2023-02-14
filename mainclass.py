from time import  sleep
from datetime import datetime
import json
from MyPyQt5 import  (
    Validation , 
    DataBase , 
    QObject,
    pyqtSignal ,

    )


class Hiraj(QObject):
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

    class PayloadQueryTypeFlags():
        FetchAds = 'FetchAds'
        comments = 'comments'
        postContact = 'postContact'
        similarPosts = 'similarPosts'
        Search = 'Search'

    class ResponseKeys():
        class Search():
            id = 'id' # Int
            authorUsername = 'authorUsername' # Str
            authorId = 'authorId'  # Int
            title = 'title' # Str
            URL = 'URL' # Str
            icon = 'icon' # Str
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


    def __init__(self) -> None:
        self.Data = DataBase('Data\DataBase.db')
        super().__init__()

    # def search(self,keyword:str,**kwargs):
    #     if "tagname" and "city" in kwargs.keys():
    #         print(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}?&tag={kwargs['tagname']}")
    #     elif "city" in kwargs.keys():
    #         print(f"https://haraj.com.sa/search/{keyword}/city/{kwargs['city']}")
    #     elif "tagname" in kwargs.keys():
    #         print(f"https://haraj.com.sa/search/{keyword}?&tag={kwargs['tagname']}")
    #     else:
    #         print(f"https://haraj.com.sa/search/{keyword}")

    def resolveSearchResponse(self,response) -> list: #  Done 
        resultIDs = []
        for Ad in response["data"]["search"]["items"] :
            id = Ad['id']
            if not self.Data.exist(table = "AdsData" ,column='id' ,val = id ):
                Ad['similarPosts'] = False
                Ad['similarPostID'] = 0
                self.Data.add_to_db(
                    table = 'AdsData' ,
                    **Ad
                    )
                resultIDs.append(id)
        return resultIDs



    def resolveCommentsResponse(self,AdID:int,AdCreatorID:int,AdCreatorUsername:str,response)-> list: # Done
        commenterIDs = []
        for comment in response["data"]['comments']['items'] :
            id = comment['id']
            if not self.Data.exist(table = "CommentsData" ,column='id' ,val = id ):
                comment['AdID'] = AdID
                comment['AdCreatorID'] = AdCreatorID
                comment['AdCreatorUsername'] = AdCreatorUsername
                self.Data.add_to_db(
                    table ='CommentsData',
                    **comment
                    )
                commenterIDs.append(comment['authorId'])
        return commenterIDs

        

    def resolvePostContactResponse(self):
        
        pass

    def resolveSimilarPostsResponse(self,response): # Done
        resultIDs = []
        similarPostID = response["data"]['similarPosts']['id']
        for Ad in response["data"]['similarPosts']['groupTags'][0]['posts']['items'] :
            id = Ad['id']
            if not self.Data.exist(table = "AdsData" ,column='id' ,val = id ):
                Ad['similarPosts'] = True
                Ad['similarPostID'] = similarPostID
                self.Data.add_to_db(
                    table = 'AdsData' ,
                    **Ad
                    )
                resultIDs.append(id)
        return resultIDs
        

        
    def resolveFetchAdsResponse(self):
        pass


    # def getQuery(self):
    #     queryfile = open('Payloads\Payload.json','r')
    #     jsonQuery = json.load(queryfile)

    #     print('\n\n')
    #     print(jsonQuery['Search'])



h = Hiraj()
h.resolveSearchResponse()
# h.getQuery()
