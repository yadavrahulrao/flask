# print("hello world")

#first program of fast api


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message":"hello world"}

  