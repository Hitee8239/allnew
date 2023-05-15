from  pandas import DataFrame as dp
from  pandas import Series

mylist=[30,40,50]
myidx=['윤봉길','김유신','신사임당']

myseries =Series(data=mylist, index=myidx)
print(myseries)

mydata = {
    '용산구':[3,12,21],
    '마포구':[6,15,24],
    '서대문구':[9,18,27]
}
myidx2=['윤봉길','김유신','이순신']
myframe= dp(data=mydata , index=myidx2)
print(myframe)

sdata = {
    '용산구':[5,20,35],
    '마포구':[10,25,40],
    '은평구':[15,30,45]
}
myidx3=['윤봉길','김유신','이완용']
myframe2=dp(data=sdata,index=myidx3)
print(myframe2)

rst=myframe.add(myseries, axis=0)
print('\nDataframe+ series')
print(rst)

rst=myframe.add(myframe2,fill_value =20)
print('\nDataframe+dataframe')
print(rst)


print('\nDataframe-dataframe')
rst=myframe.sub(myframe2,fill_value=10)
print(rst)