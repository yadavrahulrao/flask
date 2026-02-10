from fastapi import FastAPI

from fastapi.params import Body

app = FastAPI()

@app.get("/login")
async def user():
  return {"message":"login as user"}


@app.post("/create")
async def create_post(payload:dict = Body(...)):
  print(payload)
  return{"message":f"title{payload['title']} content:{payload['content']}"}