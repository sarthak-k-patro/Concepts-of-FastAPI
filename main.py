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

@app.get("/blog/unpublished")  # This should be kept above the dynamic one otherwise it will throw error, Because /blog/dynamic parameter will match if we dont keep it above dynamic parameter route
def read_blog(): # So here we are converting id into an integer
    return {"Unpublished blogs": [
        1,2,3,4,5
    ]}


# QUERY Parameters se blog aa rha hai
@app.get("/blog") # Query parameters we need not mention here in the route
def blogList(limit=0,published=False): # But function will need to aaccept the query parameters
    if(limit and published):
        return{
            "data":f"{limit} published blogs from the blog list"
        }
    elif(limit):
        return{
            "data":f"{limit} blogs from the blog list"
        }
    return{
        "blogList":{
            1:{"blog 1"},
            2:{"blog 2"},
            3:{"blog 3"},
            4:{"blog 4"},
            5:{"blog 5"},
        }
    }

# Dynamic Routing 
@app.get("/blog/{blog_id}") # From URL you will always get a string only even if you type a number it would be inside " ".
def read_blog(blog_id: int): # So here we are converting id into an integer, This is Handled by Pydantic library.
    return {"blog_id": blog_id}

