from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

from fastapi.params import Body

app = FastAPI()

# title, str , content , categery , boolean 

class Post(BaseModel):
  title :str
  content:str
  published : bool = True
  rating : Optional[int] = None



@app.post("/create")
async def create_post(new_post:Post):
  print(new_post.rating)
  return {"data":"new_post"}