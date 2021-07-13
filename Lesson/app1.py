from fastapi import FastAPI, Path
from fastapi.param_functions import Query

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

@app.get("/get-by-name")
def get_item_by_name(name:str =Query(None,title='Name',description='Item name')):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data Not Found'}

