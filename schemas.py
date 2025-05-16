from pydantic import BaseModel
from typing import List

class ActorBase(BaseModel):
    actor_name: str

class MovieBase(BaseModel):
    title: str
    year: int
    director: str
    actors: List[ActorBase]

class MoviePublic(MovieBase):
    id: int
    title: str
    year: int
    director: str
    actors: List[ActorBase]

    class Config:
        orm_mode = True
