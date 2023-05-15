import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuvO0gNCQCYze1DqtwDoHjO5Ee6VAZfJskwQ&usqp=CAU'
savename = input('저장할 파일 이름 입력 : ')

result = urllib.request.urlopen(url)

data = result.read()

with open(savename, mode="wb") as f:
    f.write(data)
    print(savename + "파일로 저장되었습니다.")