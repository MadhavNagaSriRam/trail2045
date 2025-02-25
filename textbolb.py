from textblob import TextBlob
from pydantic import BaseModel
from fastapi import FastAPI

class Items(BaseModel):
    l:list

app=FastAPI()

@app.post("/textblob")
def fun(items:Items):
    dict={}
    # text = "Indicates that the text has no particular positive or negative sentiment."
    for i in items.l:
        blob = TextBlob(i)
        polarity = blob.sentiment.polarity
        if polarity>0 :
            dict[i]="Positive"
        elif polarity<0:
            dict[i]="Negative"
        else:
            dict[i]="Neutral"
    return dict

 