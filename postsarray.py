from fastapi import FastAPI 
from pydantic import BaseModel
from random import randrange
from fastapi.params import Body

app = FastAPI()

class Post(BaseModel):
  title:str
  content : str


my_posts = [{"title":"title of post 1" , "content":"content of post 1","id":1},{"title":"rahul","content":"btech","id":2}]


@app.get("/posts")
def get_posts():
  return {"data":my_posts}


# @app.post("/posts")
# async def get_posts():
#   return {"message":my_posts}



@app.post("/posts")
async def create_posts(post : Post):
  post_dict = post.dict()
  post_dict['id'] = randrange(0,10000000)
  my_posts.append(post_dict)
  return {"data":post_dict}

