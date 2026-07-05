from fastapi import APIRouter

router=APIRouter(
    prefix='/items',
    tags=['this is route for items.']
)

@router.get('/')
def reat_items():
    return{
        'msg':'this gives you lists of items.'
    }