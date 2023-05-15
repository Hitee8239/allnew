from pandas import Series

mylist = [10,40,30,20]
myseris = Series(data=mylist ,index=['김유신','이순신','강감찬','광해군'])

print('\nData Type')
print(type(myseris))

myseris.index.name = '점수'
print('\nindex name of series')
print(myseris.index.name)

print('\nname of index')
print(myseris.name)

print('\nvalue of series')
print(myseris.values)

print('\nprint information  of series')
print(myseris)

print('\nrepeat print')
for idx in myseris.index:
    print('Index : ' + idx + ', Values : ' + str(myseris[idx]))

