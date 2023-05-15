from itertools import  count
from ChichenUtill import p340_ChickenUtill

brandName = 'pelicana'
base_url = 'https://pelicana.co.kr/store/stroe_search.html'

def getData():
    saveData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx+1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('table',attrs={'class': "tablemt20"})
        mytbody = mytable.find('tbody')
        print(mytbody)

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝 ')
