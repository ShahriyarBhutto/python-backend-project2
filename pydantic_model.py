from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

items = [
    {"id":1,"item":"A"},
    {"id":2,"item":"B"},
    {"id":3,"item":"C"}
    ]

def verify_key(key:str):
    if key != "abc123":
        raise HTTPException(status_code=401,detail="wrong key")
    return True


class Item(BaseModel):
    name:str 
    price: float
    in_stock: bool = True

app = FastAPI()

@app.get("/item")
async def get_items():
    item = Item(name = "A",price = 22.4,in_stock = False)
    return item


@app.get("/item/{id}")
async def get_item_by_id(id:int, _= Depends(verify_key)):
    for item in items:
        if item["id"] == id:
            return item
        
@app.post("/item/")
async def post_item(item:Item):
    return {"message":"Ok ho Gaya","name":item.name}






