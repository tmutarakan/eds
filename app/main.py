from fastapi import FastAPI
from app.models import User


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/users", response_model=User)
def user_root(user: User):
    return user


@app.post("/user", response_model=User)
def user_is_adutl(user: User):
    return user
