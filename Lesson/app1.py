from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {'name':'ian','date':'12/12/21'}

@app.get("/about")
def about():
    return {'Data':'Testing About'}


