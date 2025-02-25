from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['interns']  
collection = db['std_da']  

print(collection.insert_one({'id':112, 'name':'kousik','type':'o+'}))