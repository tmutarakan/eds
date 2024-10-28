from fastapi import FastAPI

from routers import user, employeer, signature


app = FastAPI()
app.include_router(user.router, prefix="/user")
app.include_router(employeer_route, prefix="/employeer")
app.include_router(signature_route, prefix="/signature")


@app.get("/")
async def root():
    return {"message": "Hello World"}
