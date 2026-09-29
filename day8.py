# curd operations 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    status : bool

@app.post("/todos")
def create(todo:Todo):
    todos.append(todo)
    return {"message":todo}

@app.get("/todos")
def get_data():
    return {"data":todos}


@app.get("/todos/{todo_id}")
def get_id_data(todo_id:int):
    for i in todos:
        if i.id == todo_id:
            return i
    return {"error : id not found"}


@app.put("/todos/{todo_id}")
def update(todo_id:int , updated: Todo):
    for i , j in enumerate(todos):
        if j.id == todo_id:
            todos[i] = updated
            return {"message": "update the data",
                    "data":updated}
    return {"error id not found"}


@app.delete("/todos/{todo_id}")

def delet(todo_id:int):
    for i , j in enumerate(todos):
        if j.id == todo_id:
            todos.pop(i)
            return {"the id data deleted"}
    return {"error id not found"}

