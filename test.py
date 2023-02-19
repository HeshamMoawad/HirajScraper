# import requests , json
# import ProxyFilterClass


# filterAPI = ProxyFilterClass.ProxyFilterAPI()


# header = {
#             'Content-Type': 'application/json' ,
#             'Accept':'*/*' ,
#             'Accept-Encoding' : 'gzip, deflate, br' ,
#             'Connection' : 'keep-alive',
#             'accept-language' : 'en-US,en;q=0.9',
#             'origin' : 'https://haraj.com.sa' ,
#             'referer' : 'https://haraj.com.sa/',
#         }

# proxy = filterAPI.getRandomProxyWithTimeOut(10)

# proxy = {'http':proxy,'https':proxy}
# print(proxy)
# Payloads = json.load(open('Payloads\Payload.json','r'))   
# payload = Payloads['postContact']
# print(payload)
# session = requests.Session()
# # session.proxies = proxy

# getres = session.get(
#     url = 'https://haraj.com.sa/'
# )

# # print(getres.request)
# print(getres.url)
# print(getres.status_code)
# # print(getres.content)


# Response = session.post(
#     url = 'https://graphql.haraj.com.sa/' ,
#     json = payload ,

# )
    
# # print(Response.request)
# print(Response.url)
# print(Response.status_code)
# print(Response.json())
    




# from seleniumwire import webdriver  # Import from seleniumwire
# from webdriver_manager.chrome import ChromeDriverManager
# IDS = []

# for i in range(3):
# # Create a new instance of the Chrome driver
#     driver = webdriver.Chrome(ChromeDriverManager().install())

#     # Go to the Google home page
#     driver.get('https://haraj.com.sa/1188478904/%D8%A7%D8%BA%D8%B1%D8%A7%D8%B6_%D8%AC%D9%8A%D8%A8_%D8%B1%D8%A7%D9%86%D8%AC%D9%84%D8%B1_%D9%88_%D9%83%D8%B4%D8%A7%D9%81_%D9%84%D9%8A%D8%AF_52_%D8%A7%D9%86%D8%B4')

#     # Access requests via the `requests` attribute
#     for request in driver.requests:
#         if request.response:
#             if 'https://graphql.haraj.com.sa/?queryName=getAnnouncement&' in request.url:
#                 id = request.url.split('clientId=')[1][:38]
#                 print(id)
#                 IDS.append(id)

# print(IDS)


# iTusena3-kaYW-JqSK-eL6E-qCw8rdpMu0Ezv3
# YP4wV1kM-oLUS-gD8L-VvWB-OSgdd7xdZx5xv3
# BaFRrNVe-obKb-vHXe-MRzb-7G1h4sN9z588v3
# Utwr3gau-b2CZ-iYzU-WZuH-bzTv2O69Q4qnv3
# nCcr0hYF-EYoW-k6Kw-BUa1-dCI5oCjCnZvDv3
# CF5sbaVK-DLIC-IgX3-Z6D2-7z4lhsur2CdAJY



# h = len('YP4wV1kM-oLUS-gD8L-VvWB-OSgdd7xdZx5xv3')

# url ='https://graphql.haraj.com.sa/?queryName=getAnnouncement&clientId=YP4wV1kM-oLUS-gD8L-VvWB-OSgdd7xdZx5xv3&version=N9.0.38%20,%202023-02-16/'

# print(url.split('clientId=')[1][:38])
# print(h)


import string
import random


example = 'Utwr3gau-b2CZ-iYzU-WZuH-bzTv2O69Q4qnv3'

# print(string.ascii_letters)

# print(lista)

# print(m)

# print()

def genLength(length):

    lista = [str(x) for x in range(10)]
    MainText = ''.join(lista) + string.ascii_letters
    return "".join([MainText[random.randint(0,38)] for x in range(length)])


def generateClientID():
    return genLength(8) + '-' + genLength(4) + '-' + genLength(4) + '-' + genLength(4) + '-' + genLength(14)

print(generateClientID())

