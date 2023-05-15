from pandas import  DataFrame as dp

sdata ={
    '국어':[40,60,80,50,30],
    '영어':[55,65,75,85,60],
    '수학':[30,40,50,60,70]
}
myidx= ['강감찬','이순신','김유신','김구','안중근']
myframe=dp(data=sdata ,index=myidx)
print(myframe)

print('\n짝수 행만 읽어보세요.')
rst =  myframe.iloc[0::2]
print(rst)

print('\n이순신 행만 시리즈로 읽어보세요.')
rst =  myframe.loc[['이순신']]
print(rst)

print('\n강감찬의 영어점수를 읽어보세요.')
rst =  myframe.loc[['강감찬'],['영어']]
print(rst)

print('\n안중근과 강감찬의 국어/수학점수를 읽어보세요.')
rst =  myframe.loc[['안중근','강감찬'],['국어','수학']]
print(rst)

print('\n이순신과 강감찬의 영어점수를 80으로 변경하세요.')
myframe.loc[['이순신','강감찬'],['영어']] = 80
print(myframe)

print('\n이순신~ 김구의 수학점수를 100으로 변경하세요.')
myframe.loc['이순신':'김구',['수학']] = 100
print(myframe)
