import requests
from bs4 import BeautifulSoup
import urllib

default_search_url = "act=2&rub=1&mainRegion=%E3%F0%E0%E4+%D1%EE%F4%E8%FF&subRegion=&regionName=%D1%EE%F4%E8%FF"
url = "https://www.imot.bg/pcgi/imot.cgi"

session = requests.Session()

response = session.get("https://www.imot.bg/")

# sofia_search_page = session.post("https://www.imot.bg/pcgi/imot.cgi", data={"act": 2, "rub": 1, "mainRegion" : "град София".encode("cp1251"), "subRegion":"", "regionName": "София".encode("cp1251")})
headers = {'Content-Type': 'application/x-www-form-urlencoded', }
# city_sofia = 'град+София'.encode('cp1251')
city_sofia=""
city = "град София".encode('cp1251')
data = {"act": 3, "rub": 1, "rub_pub_save": 1, "topmenu": 2, "actions": 1, "f0": "78.90.66.126", "f1": 1, "f2": "", "f3": "", "f4": 1, "f7": "2%7E", "f28": "", "f29": "", "f43": "", "f44": "", "f30": "EUR", "f26": "", "f27": "", "f41": 1, "f31": "", "f32": "", "f38": city, "f42": "", "f39": "", "f40": city_sofia, "fe3": "", "fe4": "", "f45": "", "f46": "", "f51": "", "f52": "", "f33": "", "f34": "", "f35": "", "f36": "", "f37": "", "fe2": 1}
concrete_search = session.post('https://www.imot.bg/pcgi/imot.cgi', data=urllib.parse.urlencode(data), headers=headers)

concrete_search.encoding = 'windows-1251'
print(concrete_search.headers)
redirect_url = concrete_search.cookies.get('imot_session_redirect')
print(redirect_url)
print(urllib.parse.parse_qsl(redirect_url))
# print(concrete_search.status_code)
# print(concrete_search.text)
# print(concrete_search.cookies.items())
# print(concrete_search.history)


