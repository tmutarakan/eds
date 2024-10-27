from fastapi import APIRouter


employeer_route = APIRouter()


@employeer_route.get('/{employeer_id}')
def get_employeer(employeer_id: int):
    return {
        "id": employeer_id,
        "name": "XYZ"
    }


@employeer_route.post('/add')
def add_employeer():
    return {
        "name": "XYZ"
    }


@employeer_route.put('/change')
def change_employeer():
    return {
        "name": "XYZ"
    }


@employeer_route.patch('/update')
def update_employeer():
    return {
        "name": "XYZ"
    }


@employeer_route.delete('/delete')
def delete_employeer():
    return {
        "name": "XYZ"
    }
