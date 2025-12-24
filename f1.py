# def get_fullname(first , last ):
#   full_name = first.title() + " " + last.title()
#   return full_name

# print(get_fullname("rahul","yadav"))



# this defines the type hints 
# def get_fullname(first:str , last:str):
#   full_name = first.title()+ " "  + last.title()
#   return full_name

# print(get_fullname("rahul" , "yadav"))



# to cancatinate we have to convert int into str .
# def name_withage(name:str , age:int):
#   older = name.title()+ "is of age :"+ str(age) 

#   return older

# print(name_withage("rahul" , 21))


# typing module declare the type annotation 

# from typing import List

# def all_items(items:list[str]):
#   for item in items:
#     print(item)

# optional used to assume str as none when not given and help to detect the error 

# from typing import Optional

# def say_hi(name : Optional[str] = None ):

#   if name is not None:
#     print(f"hey{name}")

#   else :
#     print("hello")

#pydantic model

# from datetime import datetime

# from pydantic import BaseModel

# class user(BaseModel):
#   id : int 
#   name : str = "rahul"
#   sign_up : datetime |None = None
#   friend : list[int] = []

# external_data = {
#   "id" :"123",
#   "sign_up":"2025-12-25 10:00",
#   "friend": [1,"2",b"3"],
# }

# u = user(**external_data)
# print(u)

# print(u.id)

