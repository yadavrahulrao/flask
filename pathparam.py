#path parameter 

#The value of the path parameter item_id will be passed to your function as the argument item_id.

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{items_id}")

# async def read_item(items_id):
#   return {"items_id":items_id}



#So, with that type declaration, FastAPI gives you automatic request "parsing".
# So, with the same Python type declaration, FastAPI gives you data validation.


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{items_id}")

# async def read_item(items_id : int):
#   return {"items_id": 3}



#All the data validation is performed under the hood by Pydantic

# When creating path operations, you can find situations where you have a fixed path.


#orders matters 

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/user/me")
# async def read_user_me():
#   return {"user_id":"content of user"}

# @app.get("/user/{user_id}")
# async def read_user_id(user_id :str):
#   return {"user_id": "me"}


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/user")
# async def read_user():
#   return {"rahul","rohan"}

# @app.get("/user")
# async def read_user2():
#   return {"ritik","rajbir"}



#predefined values
#If you have a path operation that receives a path parameter, 
# but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.


#enum

# from enum import Enum
# from fastapi import FastAPI

# class ModelName(str,Enum):
#   alexnet = "alexnet"
#   resnet = "resnet"
#   lenet = "lenet"

# app = FastAPI()

# @app.get("/model/{model_name}")
# async def get_model(model_name : ModelName):
#   if model_name is ModelName.alexnet:
#     return {"model_name":model_name , "mesaage":"deep learning"}
#   if model_name.value == "resnet":
#     return {"model_name":model_name,"message":"llm"}
#   return {"model_name":model_name, "message":"other"}


#OpenAPI doesn't support a way to declare a path parameter to contain a path inside,
#  as that could lead to scenarios that are difficult to test and define.



#path convertor 

from fastapi import FastAPI 

app = FastAPI()

@app.get("/file/{file_path:path}")
async def path_convert(file_path:str):
  return {"file_path":file_path}