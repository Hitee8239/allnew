from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "AppleGothic"
mylist = [30,20,40,60,50]
myidx = ['이상화','한용운','노천명','윤동주','이육사']
myseries = Series(data=mylist, index=myidx )
myylim = [0, myseries.max()+10]

myseries.plot(title='금월 실적' , kind='line' ,ylim=myylim ,grid=False  ,rot=10, use_index=True)

filename = 'seriesGraph02.png'
plt.savefig(filename , dpi=400 , bbox_inches='tight')
print(filename + 'saved')
plt.show()