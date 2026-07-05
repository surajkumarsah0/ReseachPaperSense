from fastapi import FastAPI
from pydantic import BaseModel
from users import router as user_router
from items import router as item_routes

app=FastAPI()
app.include_router(user_router)
app.include_router(item_routes)

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool = None
    


@app.get('/')
def hello():
    return {
        'msg':"hello world from the fastapi/"
    }

@app.post('/items')
def create_items(item:Item):
    return{
        'name': f'items name is {item.name}',
        'price': f'items name is {item.price}',
        'is_offer': f': {item.name}'
    }

@app.get('/items/{item_id}')
def helloid(item_id:int):
    return{'msg':f'this is coming from /items/{item_id}'}
