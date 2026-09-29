from fastapi import FastAPI

app = FastAPI() #we created the FastAPI instance here or object here.
@app.get("/") #we created the reute here

def hello():
    return {"message": "Hello Dear!"}

@app.get("/welcome") #we created the reute here
def welcome():
    return {"message": "Welcome to my first FastAPI application!"}

@app.get("/about") #we created the reute here
def about():
    return {"about me!": "This API is build by Abdulsamad"}


# This is my first FastAPI application.

