from fastapi import FastAPI

from routers import user, employeer, signature


app = FastAPI()
app.include_router(user.router, prefix="/user")
app.include_router(employeer.router, prefix="/employeer")
app.include_router(signature.router, prefix="/signature")
