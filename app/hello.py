from fastapi import FastAPI, Body


app = FastAPI()


@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}?"


@app.get("/happy")
def happy(status_code=200):
    return ":)"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
