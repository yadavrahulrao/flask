#query parameters - the parameter that are not part of path parameters
#these are given in a URL after ? , and separated by &
# query is set of key values 




from fastapi import FastAPI,Form

app = FastAPI()

# default values are given then if we dont give the values then 
@app.get("/items")
def items(skip:int = 0 , limit : int = 10):
    return {
        "skip":skip,
        "limit":limit
    }

#required query parameters - if we dont have default query paramerers , then we can take them .
@app.get("/search")
def required(q:str,a:int,b=bool):
    return {
        "query":q,
        "a":a,
        "b":b
    }


@app.get("/login")
def login(username:str,password:int):
    return {
        "status":True,
        "message":"succesfully login"
    }

@app.post("/userlogin")
def userlogin(username:str=Form(),password:int=Form()):
    return{
        "status":True,
        "message":"successful login"
    }

