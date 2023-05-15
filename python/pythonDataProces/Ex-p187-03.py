import pandas as pd
from pandas import DataFrame

myColumns =('이름','나이')
myencoding = 'utf-8'
mydata=[('김철수',10),('박영희',20)]

rst=DataFrame(data=mydata ,columns=myColumns)
print(rst)

filename = 'csv_02_01.csv'
rst.to_csv(filename,encoding=myencoding, mode="w",index=False)

filename = 'csv_02_02.csv'
rst.to_csv(filename,encoding=myencoding, mode="w",index=False, sep="#")
