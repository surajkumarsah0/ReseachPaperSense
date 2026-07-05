from fastapi import APIRouter

router=APIRouter(
    prefix='/users',
    tags=['users endpoints is this.']
)


@router.get('/')
def get_users():
    return[
        {'name':'suraj kumar sah','email':'sah@gmail.com'},
        {'name':'dipesh mahato','email':'mahato@gmail.com'},
        {'name':'ramabtar yadav','email':'yadav@gmail.com'}
    ]

@router.get('/{user_id}')
def get_user_by_id(user_id:int):
    return{
        'msg':f'the user of id {user_id} is here!'
    }