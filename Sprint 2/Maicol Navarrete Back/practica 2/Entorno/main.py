from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

movies = [
    {
        "id":1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandots viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },    
    {
        "id":2,
        "title": "gigantes de acero",
        "overview": "En un futuro no muy lejano, el boxeo robotico...",
        "year": "2011",
        "rating": 7.1,
        "category": "Drama"
    }

]
 
@app.get("/", tags=["Home"])
def home():
    return "Hello world"

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []

@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie["category"] == category:
            return movie
    return []


@app.post("/movies", tags=["Movies"])
def create_movie(
    id: int= Body(),
    title: str= Body(),
    overview: str= Body(),
    year: int= Body(),
    rating: float= Body(),
    category: str= Body()
    ):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": "year",
        "rating": rating,
        "category": category,
    })
    return movies
