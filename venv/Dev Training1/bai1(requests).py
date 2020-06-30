import requests
from bs4 import BeautifulSoup
url1='http://192.168.100.222:8888/cartmigration_ui_ver3/public'
with requests.Session() as s:
    getLoginPage = s.get(url1)
    getToken = BeautifulSoup(getLoginPage.text, 'lxml')
    token= getToken.find('input', attrs={'name': '_token'})['value']
    info = {"_token":token, "email": "test@test.com", "password": "123456"}
    login = s.post(getLoginPage.url, data=info)
    getName = BeautifulSoup(login.content, "lxml")
    print(getName.find("a", {"id": "navbarDropdown2"}).text)