from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "AppleGothic"

mylist = [30,20,40,30,60,50]
myidx = ['강감찬','김유신','이순신','안익태','윤동주','홍길동']

print(myidx)
print(mylist)
print('-'*50)

myseries = Series(data=mylist , index=myidx)
myylim = [0,myseries.max()+10]
myseries.plot(title = '시험점수', kind='line', ylim=myylim, grid=True , rot=10,use_index=True)

filename = 'seriesGraph01.png'
# plt.savefig(filename,dpi=400 , bbox_inches='tight')
print(filename + ' Saved....')
plt.show()

