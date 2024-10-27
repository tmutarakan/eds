from fastapi import FastAPI

from routers.user import user_route
from routers.employeer import employeer_route
from routers.signature import signature_route


app = FastAPI()
app.include_router(user_route, prefix="/user")
app.include_router(employeer_route, prefix="/employeer")
app.include_router(signature_route, prefix="/signature")


@app.get("/")
async def root():
    return {"message": "Hello World"}
