from fastapi import FastAPI
import os.path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
# secret_file = os.path.join(BASE_DIR, '../secret.json')

# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# def get_secret(setting, secrets=secrets):
#     try:
#         return secrets[setting]
#     except KeyError:
#         errorMsg = "Set the {} environment variable.".format(setting)
#         return errorMsg

app = FastAPI()

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/hello')
async def hello():
    return "hello World~!!"

@app.get('/random')
@app.post('/random')
async def random(max=None):
    import random
    
    if max is None:
        max = 10
        
    else:
        max = int(max)
    random_v = random.randint(1,max)
    
    return random_v
    