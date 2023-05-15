import pandas as pd
from pandas import DataFrame

filename = 'seoul.csv'
df = pd.read_csv(filename)
print(df)

rst = df.loc[(df['시군구']==' 서울특별시 강남구 신사동')]
print(rst)
print('-'*40)

rst = df.loc[(df['시군구']==' 서울특별시 강남구 신사동')& (df['단지명'] == '삼지')]
print(rst)
print('-'*40)

newdf = df.set_index(keys=['도로명'])
print(newdf)
print('-'*40)

rst = newdf.loc[['동일로']]
print(rst)
print('-'*40)
count = rst.loc['동일로'].count()
print(count)
print('-'*40)
