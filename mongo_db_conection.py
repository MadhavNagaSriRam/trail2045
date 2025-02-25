from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb://localhost:27017/")
db = client['Student_Data']
collection = db['fst_year_data']

class Data(BaseModel):
    suc_code:int
    std_name:str
    std_email:str
    std_pho:int

app = FastAPI()

def to_dict(documents):
    return {
        'Studen SUC Code':documents['Studen SUC Code'],
        'Name':documents['Name'],
        'Email Id':documents['Email Id'],
        'Phone Number':documents['Phone Number']
        }

@app.post("/db_storage")
def std_data(items:Data):
    if(collection.insert_one({'Studen SUC Code':items.suc_code,'Name':items.std_name,'Email Id':items.std_email,'Phone Number':items.std_pho})):
        return "SucessFul"
    else:
        return "Not Register"

@app.get("/db_display")
def extract_data():
    documents = collection.find()
    l=[]
    for i in documents:
        x = to_dict(i)
        l.append(x)
    return l
