# print("hello world")

#first program of fast api


from fastapi import FastAPI

app = FastAPI()

@app.get("/login")
async def root():
  return {"message":"hello world"}

@app.get("/posts")
def get_posts():
  return {"data": "this will provide a posts"}