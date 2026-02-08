from typing import Optional
from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel 
from random import randrange


app = FastAPI()

class Post(BaseModel):
  title : str 
  content : str
  published : bool = True 
  rating : Optional[int] = None





my_posts = [{"title" : "title of post 1","content": "content of post 1","id":1},{
  "title":"food","content":"pizza","id":2}]

