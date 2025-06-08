from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    msg="Hello World!"
    return msg