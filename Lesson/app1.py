from fastapi import FastAPI, Path

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
        "price":3,
        "brand": "KCC"
        },
    2: {
        "name":"soda",
        "price":8,
        "brand": "Cocacola"
        }
}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None,description='The ID of the item you would like to view',gt=0,lt=2)):
    return inventory[item_id]



