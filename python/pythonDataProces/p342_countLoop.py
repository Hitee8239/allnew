from itertools import count

for page_idx in count():
    if page_idx >= 5:
        break
    print(page_idx)
print('finished')


## p350_getPelicanaStore.py

from itertools import count
from p340_ChickenUtill import ChickenStore

brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store/stroe_search.html'

def getData():
    savedData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        # print( url )
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('table', attrs={'class': 'table mt20'})
        mytbody = mytable.find('tbody')
        print(mytbody)

print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')