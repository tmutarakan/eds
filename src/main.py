from fastapi import FastAPI
import uvicorn

from router import user, employeer, signature


app = FastAPI()
app.include_router(user.router)
app.include_router(employeer.router)
app.include_router(signature.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
