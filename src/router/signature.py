from fastapi import APIRouter


router = APIRouter(prefix="/signature")


@router.get('/')
def get_all():
    return {
        "name": "XYZ"
    }


@router.get('/{user_id}')
def get_one(user_id: int):
    return {
        "id": user_id,
        "name": "XYZ"
    }


@router.post('/')
def create():
    return {
        "name": "XYZ"
    }


@router.patch('/')
def modify():
    return {
        "name": "XYZ"
    }


@router.put('/')
def replace():
    return {
        "name": "XYZ"
    }


@router.delete('/')
def delete():
    return {
        "name": "XYZ"
    }
