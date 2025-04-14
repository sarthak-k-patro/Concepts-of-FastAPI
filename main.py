from fastapi import FastAPI

app=FastAPI() # Creating instance of FastAPI


@app.get('/')
def index():
    return {
        "data":{
        "Name":"Sarthak",
        "age":"25"
    }}

@app.get("/about")
def about():
    return {"data": "This is about page"}