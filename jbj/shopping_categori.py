import os
import sys
import urllib.request,datetime, math, json
import pandas as pd


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
    
    

client_id= get_secret("NAVER_API_ID")
client_secret = get_secret('NAVER_API_KEY')
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2021-01-01\",\"endDate\":\"2023-05-23\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"원피스\",\"keywords\":[\"원피스\"]},{\"groupName\":\"티셔츠\",\"keywords\":[\"티셔츠\"]},{\"groupName\":\"반팔\",\"keywords\":[\"반팔\"]},{\"groupName\":\"바지\",\"keywords\":[\"바지\"]},{\"groupName\":\"재킷\",\"keywords\":[\"재킷\"]}]}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
result = json.loads(response.read().decode('utf-8'))
# print(result)

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    # print('-'*50)
else:
    print("Error Code:" + rescode)
res = result["results"]
df = pd.DataFrame(res)
print(df)