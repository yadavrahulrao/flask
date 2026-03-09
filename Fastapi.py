# import fastapi

# print(fastapi.__version__)


# from fastapi import FastAPI,Request
# from mockdata import products

# app = FastAPI()



# @app.get("/")
# def home():
#   return "welcome rahul !"

# @app.get("/con")
# def contact():
#   return "you are the connection"


# @app.get("/pro")
# def product():
#   return products


# path parameters 
# @app.get("/product/{product_id}")
# def get_one_product(product_id:int):

#   # if product avialable with id , return product 

#   product = None
#   for i in products:
#     if i.get("id") == product_id:
#       return i

#   return {
#     "error":"product not found for this id"
#   }


#query parameters 
# @app.get("/greet")
# def greet_user(name:str,age:int):
#   return {
#     "greet":f"hello {name} ,age is {age}!"
#   }


# @app.get("/greet")
# def greet_user(request:Request):
#   d = dict(request.query_params)
#   print(d)
#   return{
#     "greet":f"hello {d.get("name")} , age is{d.get("age")}"
#   }




# http methods 
# how to validate data

from fastapi import FastAPI,Request
from mockdata import products
from Dtos import ProductDTO


app = FastAPI()


# dtata sends through body , request header , query params 
@app.post("/create")
def create_product(data:ProductDTO):

  data = data.model_dump()
  print(data)
  products.append(data)

  # dic = dict(data)
  # print(dic)
  return {
    "status":"created a product",
    "data":products
  }


# pydantic is  module to provide data types for python 
# using this we can implement data validation

#postman 


@app.get("/product/{product_id}")
def get_one_product(product_id:int):

  product = None
  for i in products:
    if i.get("id") == product_id:
      return i
    
  return{
    "error":"id not found !!!"
  }


@app.put("/update/{product_id}")
def update_product(data:ProductDTO,product_id:int):

  for idx,i in enumerate(products):
    if i.get("id") == product_id:
      products[idx] == data.model_dump()
      return{
        "status":"updated",
        "product":data
      }
  print(i,idx)
  return {
    "status":"id not found"
  }


@app.delete("/delete/{product_id}")
def delete_product(product_id:int):
  for idx , i in enumerate(products):
    if i.get("id") == product_id:
      delet= products.pop(idx)

    return{
      "status":"deleted",
    
    }