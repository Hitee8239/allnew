import time
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from collections import deque

f = open("weather_data.txt", 'r', encoding='utf-8')
weather = ""
i = 1
f.readline()

dq = deque()

yy = 2019
mm = 0

dd = 1
while True:
    temp = f.readline()
    row1 = temp.split('\t')
    temp = f.readline()
    row2 = temp.split('\t')
    # print(row1, row2)
    for i in range(len(row1)):
        value = {}
        if len(row1[i]) > 0:
            # print(row1[i].split('일')[0])
            try:
                dd = int(row1[i].split('일')[0])
                if dd == 1:
                    if mm <= 11:
                        mm += 1
                    else:
                        mm = 1
                        yy += 1
            except:
                if row1[i].split('일')[0] == '\n':
                    continue

            value['날짜'] = str(yy) + '-' + str(mm).zfill(2) + '-' + str(dd).zfill(2)
            row2[i] = row2[i].replace(' -', '0')
            for r in row2[i].split(' '):
                if len(r) > 1:
                    # print(r.split(':'))
                    val = r.split(':')[1]
                    val = val.replace('\n','')
                    value[r.split(':')[0]] = val
        if len(value) > 0:
            dq.append(value)
            # print(value)
    if not temp:
        break
    weather += temp
f.close()
# for d in dq:
#     print(d)
df = pd.DataFrame(dq, columns=list(dq[0].keys()))
# print(df)
df = df.dropna()
# print(df)

df.to_csv('WEATHER.csv', encoding='utf-8', index=False)

df1 = pd.read_csv('WEATHER.csv', encoding='utf-8')
df1['평균기온'] = df1['평균기온'].str[:-1]
df1['최고기온'] = df1['최고기온'].str[:-1]
df1['최저기온'] = df1['최저기온'].str[:-1]
df1['일강수량'] = df1['일강수량'].str.replace('mm','')
# print(df1)

df1 = df1.astype({'평균기온': 'float', '최고기온': 'float','최저기온': 'float','평균운량': 'float','일강수량': 'float'})
# print(df1.info())



