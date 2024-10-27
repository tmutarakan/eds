from fastapi import APIRouter


user_route = APIRouter()


@user_route.get('/{user_id}')
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "XYZ"
    }


@user_route.post('/add')
def add_user():
    return {
        "name": "XYZ"
    }


@user_route.put('/change')
def change_user():
    return {
        "name": "XYZ"
    }


@user_route.patch('/update')
def update_user():
    return {
        "name": "XYZ"
    }


@user_route.delete('/delete')
def delete_user():
    return {
        "name": "XYZ"
    }
