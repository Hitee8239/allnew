from pandas import  Series

mylist1 = [40,50,60]
mylist2 = [20,40,70]
myidx1= ['성춘향','이몽룡','심봉사']
myidx2= ['성춘향','이몽룡','뺑덕어멈']

myseries1 = Series(data=mylist1 ,index=myidx1)
myseries2 = Series(data=mylist2 ,index=myidx2)

print(myseries1)
print(myseries2)
print('-'*40)
sumseries = myseries1.add(myseries2,fill_value=10)
print(sumseries)

subseries = myseries1.sub(myseries2, fill_value=30)
print(subseries)