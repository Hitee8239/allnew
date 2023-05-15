import numpy as np
import pandas as pd
from pandas import  DataFrame, Series

sdata = {
    '국어':[60.00,np.nan,40.00],
    '영어':[np.nan,80.00,50.00],
    '수학':[90.00,50.00,np.nan]
}
myidx = ['강감찬','김유신','이순신']

print('#Before')
myframe = DataFrame(data=sdata,index=myidx)
print(myframe)

myframe.loc[myframe['국어'].isnull(),'국어']=myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(),'영어']=myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(),'수학']=myframe['수학'].mean()


print('#After')
print(myframe)


