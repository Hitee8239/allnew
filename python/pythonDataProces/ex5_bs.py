from bs4 import BeautifulSoup
from pandas import  DataFrame as df
import matplotlib.pyplot as plt
import  numpy as np

html = open('ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
result = []
tbody = soup.find("tbody")
tds = tbody.find_all('td')
for data in tds:
    result.append(data.text)
print(result)
print('-'*50)
mycolumns = ['이름','국어','영어']

myframe= df(np.reshape(np.array(result),(4,3)),
            columns=mycolumns)
myframe= myframe.set_index('이름')
print(myframe)

plt.rcParams['font.family'] = "AppleGothic"

myframe.astype(float).plot(title='Score' , kind='line', grid=False, rot=10, use_index=True)

filename = 'quiz.png'
plt.savefig(filename , dpi=400 , bbox_inches='tight')
print(filename + 'saved')
plt.show()

