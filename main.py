from fastapi import FastAPI

app=FastAPI() # Creating instance of FastAPI


@app.get('/') # The decorator path matters
def index():  # function name could be anything it doesn't matter
    return {
        "data":{
        "Name":"Sarthak",  # From line 7 to 12 its called path operation function. Operation means GET,POST, DELETE etc
        "age":"25"
    }}

@app.get("/about") # Here its called path not route or endpoints
def about():    
    return {"data": "This is about page"}

@app.get("/blog/{blog_id}") # From URL you will always get a string only even if you type a number it would be inside " ".
def read_blog(blog_id: int): # So here we are converting id into an integer
    return {"blog_id": blog_id}