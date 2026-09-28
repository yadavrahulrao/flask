from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def home():
#     return {"this is the message"}


# path parameters 
# dynamic routing 
# @app.get("/user/{user_id}")
# def user(user_id):
#     return {"user":user_id}


# # validation of different datatypes 
# @app.get("/user/{user_id}")
# def user(user_id:int):
#     return {"user":user_id}


# query parameters - / user?124

# @app.get("/user")
# def user(name:str):
#     return {"message":name}


#optional parameters 
# @app.get("/users")
# def user(name:str = None):
#     return {"message":name}


# default values 
# @app.get("/product")
# def products(limit=10):
#     return {"limit":limit}


# multiple query parameters 

# @app.get("/items")
# def items(name:str = None , id : int = 0):
#     return {"name":name ,
#             "id":id}




#Request body
# post request

# @app.post("/create")
# def user(name:str , age : int):
#     return {"name":name , "age":age}

# data in the form of json 
# there is no validation in it so we use pydantic 
# @app.post("/create")
# def user(data:dict):
#     return {"message":"data added",
#             "data":data
#     }


# from pydantic import BaseModel


# class User(BaseModel):
#     name : str 
#     age : int 

# @app.post("/create")
# def user(data:User):
#     return {"message":"data added",
#             "data":data
#     }



# pydantic model - schemas 

# class User(BaseModel):
#     name: str
#     age : int 
#     email: str

# @app.post("/create")
# def user(data:User):
#     return {"message":"created",
#             "data":data}


# nested models 

class Address(BaseModel):
    city : str
    pincode : int

class User(BaseModel):
    name : str
    age : int 
    address : Address

@app.post("/create")
def user(data:User):
    return {"message":"created",
            "data":data}