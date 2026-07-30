from fastapi import FastAPI

website = FastAPI()

@website.get("/home")
def home():
    return "Home is a function"

@website.get("/about")
def about():
    return "about is a function"

@website.get("/blogs")
def blogs():
    return "blogs is a function"
