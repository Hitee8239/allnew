import numpy as np
import pandas as pd

from pandas import  Series, DataFrame

print('\n#시리즈의 누락된 데이터 처리하기')
print('#원본 시리즈')
myseries = Series(['강감찬','이순신',np.NaN,'광해군'])
print(myseries)
print('-'*40)

print('\n#isnull() 함수 : NaN이면 True')
print(myseries.isnull())
print('-'*40)

print('\n#notnull() 함수 : NaN이아니면  True')
print(myseries.notnull())
print('-'*40)

print('\n#notnull() 함수를 이용하여 참인 항목만 출력 ')
print(myseries[myseries.notnull()])
print('-'*40)

print('\n#isnull() 함수를 이용하여 nan인 항목만 출력 ')
print(myseries[myseries.isnull()])
print('-'*40)

print('\n# dropna() 이용하여 누락 데이터 처리 ')
print(myseries.dropna())
print('-'*40)

filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)
print('-'*40)

print('\n# dropna() 이용 누락데이터 처리')
cleaned = myframe.dropna(axis=0)
print(cleaned)
print('-'*40)

print('\n# how="all"이용 누락 데이터 처리  ')
cleaned = myframe.dropna(axis=0,how='all')
print(cleaned)
print('-'*40)

print('\n# how="any"이용 누락 데이터 처리  ')
cleaned = myframe.dropna(axis=0,how='any')
print(cleaned)
print('-'*40)

print('\n# [영어] 컬럼에 NaN 제거 ')
cleaned = myframe.dropna(subset=['영어'])
print(cleaned)
print('-'*40)

print('\n# 컬럼기준 how="all" 이용 누락 데이터 처리 ')
cleaned = myframe.dropna(axis=1,how='all')
print(cleaned)
print('-'*40)

print('\n# 컬럼기준 how="any" 이용 누락 데이터 처리 ')
cleaned = myframe.dropna(axis=1,how='any')
print(cleaned)
print('-'*40)

print('##before :')
print(myframe)
myframe.loc[['강감찬','홍길동'],['국어']]=np.nan
print('## after')
print(myframe)
print('-'*40)

print(myframe.dropna(axis=1,how='all'))
print('-'*40)

print('## thresh option')
print(myframe.dropna(axis=1 , thresh=2))
print('-'*40)

print(myframe.dropna(axis=1 , how='any'))
print('-'*40)