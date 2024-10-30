from fastapi import APIRouter
from model.employeer import Employeer
import service.employeer as service


router = APIRouter(prefix="/employeer")


@router.get('/')
def get_all() -> list[Employeer]:
    return service.get_all()


@router.get('/{id}')
def get_one(employeer_id: int) -> Employeer | None:
    return service.get_one(employeer_id)


@router.post('/')
def create(employeer: Employeer) -> Employeer:
    return service.create(employeer)


@router.patch('/')
def modify(employeer: Employeer) -> Employeer:
    return service.modify(employeer)


@router.put('/')
def replace(employeer: Employeer) -> Employeer:
    return service.replace(employeer)


@router.delete('/{id}')
def delete(employeer_id: int) -> None:
    return service.delete(employeer_id)
