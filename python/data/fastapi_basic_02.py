from fastapi import FastAPI
from pydantic.main import BaseModel

class HelloWorldRequest(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get(path='/')
async def hello():
    return "hello world~!"

@app.get(path='/hello/{name}')
async def hello_with_name(name:str):
    return "hello with name . your name is "+ name

@app.get(path='/hello/query')
async def hello_with_querystring(name:str):
    return "hello with name . your name is "+ name

@app.post(path='/hello/post')
async def hello_post(request: HelloWorldRequest):
    return "hello with post . your name is {}, your age is {}".format()(request.name , request.age) 
    