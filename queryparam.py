# query parameters

#When you declare other function parameters that are not part of the path parameters, 
# they are automatically interpreted as "query" parameters.

#The query is the set of key-value pairs that go after the ? in a URL, 
# separated by & characters.


# from fastapi import FastAPI

# app = FastAPI()

# fake = [{"name":"foo"},{"name":"bar"},{"name":"rao"}]

# @app.get("/items/")
# async def read_items(skip:int = 0 , limit: int = 10):
#   return fake[skip: skip + limit]


#optional parameters

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{items_id}")
async def read_item(item_id:str , q : str | None = None):
  if q:
    return {"item_id":item_id , "q": q}
  return{"item_id":item_id}