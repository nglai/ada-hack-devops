from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    name: str
    eats: str
    plays: str
    lives: str
