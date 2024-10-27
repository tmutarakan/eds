from fastapi import APIRouter


signature_route = APIRouter()


@signature_route.get('/{signature_id}')
def get_signature(signature_id: int):
    return {
        "id": signature_id,
        "name": "XYZ"
    }


@signature_route.post('/add')
def add_signature():
    return {
        "name": "XYZ"
    }


@signature_route.put('/change')
def change_signature():
    return {
        "name": "XYZ"
    }


@signature_route.patch('/update')
def update_signature():
    return {
        "name": "XYZ"
    }


@signature_route.delete('/delete')
def delete_signature():
    return {
        "name": "XYZ"
    }
