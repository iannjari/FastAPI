from typing import Optional
from fastapi import FastAPI, Path
from fastapi.param_functions import Query
from typing import Optional
from pydantic import BaseModel
app= FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]= None

class UpdateItem(BaseModel):
    name: Optional[str]= None
    price: Optional[float]= None
    brand: Optional[str]= None


@app.get("/")
def home():
    return {'name':'ian','date':'12/12/21'}

@app.get("/about")
def about():
    return {'Data':'Testing About'}

inventory= {
    
}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None,description='The ID of the item you would like to view',gt=0)):
    if item_id in inventory:
        return inventory[item_id]
    return {'Data Not Found'}
@app.get("/get-by-name")
def get_item_by_name(name:str =Query(None,title='Name',description='Item name')):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {'Data Not Found'}

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return {'Error':'Item ID already exists'}
    inventory[item_id]= item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    
    if item_id not in inventory:
        return {'Error':'Item ID does not exist'}
    
    if item.name!= None:
        inventory[item_id].name= item.name
    if item.price!= None:
        inventory[item_id].price= item.price
    if item.brand!= None:
        inventory[item_id].brand= item.brand

    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id:int= Query(...,description='Item ID of item to delete',gt=0)):
    
    if item_id not in inventory:
        return {'Error':'Item ID does not exist'}
    del inventory[item_id]
    return {'Sucessfully Deleted'}