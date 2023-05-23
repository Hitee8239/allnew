#-*- coding: utf-8 -*-
import os
import sys
import urllib.request,datetime, math, json

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
        # print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
def getSearchData():
    client_id= get_secret("NAVER_API_ID")
    client_secret = get_secret('NAVER_API_KEY')

    end_point = "https://openapi.naver.com/v1/datalab/shopping/categories";
    body = "{\"startDate\":\"2023-05-20\",\"endDate\":\"2023-05-23\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"패션의류\",\"param\":[\"50000000\"]},{\"name\":\"화장품/미용\",\"param\":[\"50000002\"]},{\"name\":\"패션잡화\",\"param\":[\"50000001\"]}}";

    request = urllib.request.Request(end_point)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")

    
    
#     url = end_point+str(request) + body
#     print(url)
# getSearchData()
    
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        # print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None