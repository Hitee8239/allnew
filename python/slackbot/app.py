from slack_sdk import WebClient
import os.path
import requests
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse
import json
from slack_sdk import WebClient

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg
        
UserToken = get_secret('slack_UserOAuthToken')
BotToke = get_secret('slack_BotOAuthToken')
channel_name = "#project"

@app.get(path='/')
async def health_check():
    return "OK"

if __name__ == "__main__":
    nvicorn.run(app, hosh="0.0.0.0", port = 3000)
    
    
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers = {"Authorization" : "Bearer " + token},
        data = {"channel":channel, "text":text}
    )
    

@app.post(path='/sendUserchat')
async def sendUserChat(text:str):
    post_message(UserToken,channel_name,text)
    return {f'message:{text}'} 

@app.post(path='/sendBotchat')
async def sendBotChat(text:str):
    post_message(BotToke,channel_name,text)
    return {f'message:{text}'} 

@app.post(path='/sendhook')
async def sendHook(text:str):
    webhookToken = get_secret("slack_woob")
    cmd = "curl -X POST -H " 
    cmd += "'Content-type: application/json' —data "
    cmd += "'{" + '"text"' + ":" + '"' + text + '"' + "}' "
    cmd += webhookToken    
    os.system(cmd)
    return cmd 

