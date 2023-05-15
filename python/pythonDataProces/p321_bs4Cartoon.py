from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


myurl = 'https://comic.naver.com/webtoon/weekday.naver'

response = urlopen(myurl)

print(type(response))

soup = BeautifulSoup(response,'html.parser')

title= soup.find('title').string
print(title)