from fastapi import FastAPI

app = FastAPI()

@app.get("/posts/{id}")
async def get_posts(id):
  print(id)
  return {"message": f"this is the{id} "}