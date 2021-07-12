from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {'name':'ian','date':'12/12/21'}

@app.get("/about")
def about():
    return {'Data':'Testing About'}

inventory= {
    1: {
        "name":"milk",
        "price":3
        "brand": "KCC"
        },
    2: {
        "name":"soda",
        "price":8
        "brand": "Cocacola"
        }
}
