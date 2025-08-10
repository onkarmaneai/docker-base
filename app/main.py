from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Docker!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/status")
def get_status():
    return {"status": "running", "version": "1.0.0"}

