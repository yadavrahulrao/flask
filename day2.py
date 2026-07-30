# dynamic url

from fastapi import FastAPI

app = FastAPI()


@app.get("/profile/{name}")
def dynamic(name):
    return f"you added a {name} the profile added"


@app.get("/{name}/{age}")
def age(name,age):
    return f"{name} is {age} years old"