from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get(path='/')
def Check():
    return "ok"

@app.get('/getcsv')
def getcsv():
    csv_file = 'data.csv'
    
    df = pd.read_csv(csv_file)
    dict_data = df.to_dict()
    
    return dict_data