from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

class User(BaseModel):
    username:str
    email:str


@router.get('/register')
def register_user():
    return{
        'status':'success',
        'msg':"register route is triggered!"
    }