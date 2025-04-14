from fastapi import FastAPI
from . import schemas
app=FastAPI()

# @app.post("/")
# def create_post(title,body): This is a bad way of doing, we need pydantic to define structure and validate
#     # return {
#     #     "title": title,
#     #     "body": body
#     # }

# Using Pydantic: check schemas.py for the pydantic

# Now to store this we need to connect to sql database
@app.post('/createblog')
def create_blog(request:schemas.blog_model):
    return{
        "title":request.title,
        "body":request.body,
        # "id":request.id
    }