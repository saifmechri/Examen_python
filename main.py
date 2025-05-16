from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_index():
    return FileResponse("index.html")  # fichier à la racine
@app.get("/movies/", response_model=List[schemas.MoviePublic])
def read_movies(db: Session = Depends(get_db)):
    movies = db.query(models.Movies).all()
    return movies

@app.post("/movies/", response_model=schemas.MoviePublic)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = models.Movies(
        title=movie.title,
        year=movie.year,
        director=movie.director
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    for actor_data in movie.actors:
        db_actor = models.Actors(actor_name=actor_data.actor_name, movie_id=db_movie.id)
        db.add(db_actor)
    db.commit()

    return db_movie
