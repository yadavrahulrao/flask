from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

class Movie(BaseModel):
    name: str
    release_date: date
    cast: List[str]
    rating: float
    director: str
    description: str | None = None

movies: List[Movie] = []

@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie):
    movies.append(movie)
    return movie

@app.get("/movies", response_model=List[str])
def list_movie():
    return [m.name for m in movies]
