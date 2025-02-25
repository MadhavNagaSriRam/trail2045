# base 64 soft copy
# import base64
# string_input=input()
# encode_data=base64.b64encode(string_input.encode('utf-8'))
# print(encode_data)
# decode_data=base64.b64decode(encode_data).decode('utf-8')

from fastapi import FastAPI
from pydantic import BaseModel
import csv

# Create an instance of FastAPI
app = FastAPI()

# Define the data model
class Items(BaseModel):
    name: str
    ph: int
    email: str

# Create a POST endpoint to append data to the CSV
@app.post('/locustt')
def loc(items: Items):
    # Data to be appended
    new_row = [items.name, items.ph, items.email]

    # Append the data to the CSV file
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
    return {"message": "Data appended successfully."}