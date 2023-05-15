from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body= soup.select_one("body")
ptag = body.find('p')
print('1번째 P태그 : ', ptag['class'])

ptag['class'][1] = 'white'

print('1번째 p 태그 :', ptag['class'])

ptag['id'] = 'apple'

print('1번째 p 태그의 id  :', ptag['id'])

body_tag = soup.find('body')
print(body_tag)

idx = 0
print('children 속성으로 하위 항목 보기 ')
print('white character 문자까지 포함됨 ')
for child in body_tag.children:
    idx += 1
    print(str(idx)+ '번째 요소 : ' , child)

mydiv = soup.find('div')
print(mydiv)

print('div태그의 부모 태그는')
print(mydiv.parent)

mytag = soup.find("p", attrs={'class':'hard'})
print(mytag)

print('mytag 태그의 부모 태그는? ')
print(mytag.find_parent())

print('mytag 태그의 모든 상위  부모 태그는? ')
parents = mytag.find_parents()
for p in parents :
    print(p.name)
print('-'*50)
