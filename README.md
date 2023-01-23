# finetuned-Distilbert-bbc-news-classification-

The goal of the project is to identitfy the topic/class of the News Article. i.e. What is the category of the article among 5 categories : ***business, entertainment, politics, sport, tech***. </br>
I have finetuned DistilBERT on the BBC News Classification Dataset using Hugging Face Trainer API and then created a RestAPI using FastAPI and Docker.

## Dataset Introduction: 

Source: (http://mlg.ucd.ie/datasets/bbc.html)
All rights, including copyright, in the content of the original articles are owned by the BBC.</br>

Consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005.
Class Labels: 5 (business, entertainment, politics, sport, tech)


## Training Results:
<img width="650" alt="Screen Shot 2023-01-23 at 4 52 47 PM" src="https://user-images.githubusercontent.com/63723023/214170795-e32bae52-bb69-4f80-814a-25169d8cf126.png">

## API Demo:
![](distilbert_api-demo.gif)






