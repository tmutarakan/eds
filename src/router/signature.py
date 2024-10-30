from fastapi import APIRouter
from model.signature import Signature
import service.signature as service


router = APIRouter(prefix="/signature")


@router.get('/')
def get_all() -> list[Signature]:
    return service.get_all()


@router.get('/{filename}')
def get_one(filename: str):
    return service.get_one(filename)


@router.post('/')
def create(signature: Signature):
    return service.create(signature)


@router.patch('/')
def modify(signature: Signature):
    return service.modify(signature)


@router.put('/')
def replace(signature: Signature):
    return service.replace(signature)


@router.delete('/')
def delete(filename: str):
    return service.delete(filename)
