import requests , json
import ProxyFilterClass


filterAPI = ProxyFilterClass.ProxyFilterAPI()


header = {
            'Content-Type': 'application/json' ,
            'Accept':'*/*' ,
            'Accept-Encoding' : 'gzip, deflate, br' ,
            'Connection' : 'keep-alive',
            'accept-language' : 'en-US,en;q=0.9',
            'origin' : 'https://haraj.com.sa' ,
            'referer' : 'https://haraj.com.sa/',
        }

proxy = filterAPI.getRandomProxyWithTimeOut(10)

proxy = {'http':proxy,'https':proxy}
print(proxy)
Payloads = json.load(open('Payloads\Payload.json','r'))   
payload = Payloads['postContact']
print(payload)
session = requests.Session()
# session.proxies = proxy

Response = session.post(
    url = 'https://graphql.haraj.com.sa/' ,
    json = payload ,

)
    
print(Response.request)
print(Response.url)
print(Response.status_code)
print(Response.json())
    





