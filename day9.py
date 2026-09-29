#response model 

from fastapi  import FastAPI,status,HTTPException , Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     # validation
#     name:str
#     age:int
#     password:str


# class UserResponse(BaseModel):
#     name:str
#     age:int

# @app.get("/user",response_model= UserResponse)   # response model for hiding the sensitive data
# def get_data():
#     #output formatting 
#     return {"name":"MOHIT",
#             "age":39,
#             "password":"12sdkdjfsgh"
#             }







# status code 
# 200 - ok 


# @app.post("/user",status_code = status.HTTP_201_CREATED)
# def create_user():
#     return {"message":"user created"}



# custom response 
# @app.get("/user")
# def get_user():
#     return {
#         "status":"success",
#         "fetch":"user fetch",
#         "data":{
#             "name":"rahul",
#             "age":30
#         }
#     }

#exception handling 
# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code = 404,
#             detail = "user not found"
#         )
#     return {
#         "id" : 1,
#         "name" :"mohit" 
#     }



# custom exception 

# class UserNotFound(Exception):
#     def __init__(self,name:str):
#         self.name = name
    
# @app.exception_handler(UserNotFound)
# def usernotfound(request:Request,exception: UserNotFound):
#     return JSONResponse(
#         status_code=404,
#         content = {
#             "status" : "error",
#             "message": f"user exception :{exception.name}"
#         }
#     )


# @app.get("/user/{name}")
# def get_user(name:str):
#     if name != "mohit":
#         raise UserNotFound(
#             name
#         )
#     return {
#         "name":name
#     }

# # to make a error more powerful - global error handler




