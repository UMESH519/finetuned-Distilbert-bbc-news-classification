from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
import numpy as np
import torch
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from pydantic import BaseModel
import re
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse





app= FastAPI()


#first route
@app.get("/")
def get_root():
    return {"Hello": "Welcome to the News Classification API"}


def clean_text(text):

    text = text.lower().strip()     
    text = re.sub("[^A-Za-z0-9]+", " ", text)
    text = re.sub(" +", " ", text)

    return text




class NewsText(BaseModel):
    text: str






def get_model():
    tokenizer =  AutoTokenizer.from_pretrained("Umesh/distilbert-bbc-news-classification")
    model = AutoModelForSequenceClassification.from_pretrained("Umesh/distilbert-bbc-news-classification")
    return model,tokenizer

model,tokenizer =get_model()

d ={
    
     0: "business",
     1: "entertainment",
     2:"politics",
     3:"sport",
     4:"tech"
    
    }


@app.post("/predict")
async def read_root(input:NewsText):


    user_input = input.text
    cleaned_text = clean_text(user_input)


    test_sample = tokenizer([cleaned_text],padding=True,max_length=512,truncation=True,return_tensors='pt')
    output = model(**test_sample)
    y_pred = np.argmax(output.logits.detach().numpy(),axis=1)
    response= {"Recieved Text" :user_input,"Predcition": d[y_pred[0]]}

    return response




'''

@app.post("/predict")
async def read_root(input:NewsText):


    user_input = input.text
    cleaned_text = clean_text(user_input)


    test_sample = tokenizer([cleaned_text],padding=True,max_length=512,truncation=True,return_tensors='pt')
    output = model(**test_sample)
    y_pred = np.argmax(output.logits.detach().numpy(),axis=1)
    response= {"Recieved Text" :user_input,"Predcition": d[y_pred[0]]}

    return response

'''