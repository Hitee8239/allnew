import json, urllib.request, datetime, math
import os.path
from pprint import pprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../python/secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

now = datetime.datetime.now()
base_date = now.strftime('%Y%m%d')
# print(base_date)
# print(now.strftime('%H00'))
def getWeatherData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'

    parameters = ''
    parameters += "?serviceKey=" + get_secret("data_apiKey")
    parameters += "&pageNo=" + str(pageNo) 
    parameters += "&numOfRows=" + str(numOfRows)
    parameters += "&dataType=JSON"
    parameters += "&base_date="+now.strftime('%Y%m%d')
    parameters += "&base_time=0500"
    parameters += "&nx=55"
    parameters += "&ny=127"
    
    url = end_point + parameters

    print('URL')
    print(url)

    result = getRequestUrl(url)
    print(result)
    if (result == None):
        return None
    else:
        return json.loads(result)
jsonResult = []

pageNo = 1  
numOfRows = 100 
weatherData=getWeatherData(pageNo,numOfRows)
if weatherData is not None:
    print('check')
    pass
nPage = 0
while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getWeatherData(pageNo, numOfRows)
    pprint(jsonData)

    if (jsonData['response']['header']['resultCode'] == '00'):
        totalCount = jsonData['response']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)  
        categori = jsonData['response']['body']['items']['item']
        for item in jsonData['response']['body']['items']['item']:
            
            jsonResult.append(item)

        if totalCount == 0:
            break
        nPage = math.ceil(totalCount / numOfRows)
        if (pageNo == nPage):  
            break  

        pageNo += 1
    else :
        break

    savedFilename = 'nowWeather.json'
    with open(savedFilename, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    
    print(savedFilename + ' file saved..')

 
# POP	강수확률
# PTY	강수형태
# PCP	1시간 강수량
# REH	습도
# SNO	1시간 신적설
# SKY	하늘상태
# TMP	1시간 기온
# TMN	일 최저기온
# TMX	일 최고기온
# UUU	풍속(동서성분)
# VVV	풍속(남북성분)
# WAV	파고
# VEC	풍향
# WSD	풍속
# T1H	기온
# RN1	1시간 강수량
# UUU	동서바람성분
# VVV	남북바람성분
# REH	습도
# PTY	강수형태
# VEC	풍향
# WSD	풍속
# T1H	기온
# RN1	1시간 강수량
# SKY	하늘상태
# UUU	동서바람성분
# VVV	남북바람성분
# REH	습도
# PTY	강수형태
# LGT	낙뢰
# VEC	풍향
# WSD	풍속
