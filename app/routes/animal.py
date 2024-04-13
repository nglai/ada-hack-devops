from fastapi import APIRouter, HTTPException
from ..models import Animal

router = APIRouter()

# Lista estática de animais
animals = [
    Animal(id=1, name="Leão", eats="Carne", plays="Corrida", lives="Savana"),
    Animal(id=2, name="Girafa", eats="Folhas", plays="Alcançar alturas", lives="Savana"),
    Animal(id=3, name="Urso Panda", eats="Bambu", plays="Rolagem", lives="Florestas"),
    Animal(id=4, name="Golfinho", eats="Peixes", plays="Saltos", lives="Oceanos"),
    Animal(id=5, name="Águia", eats="Peixes", plays="Voo alto", lives="Montanhas"),
    Animal(id=6, name="Tigre", eats="Carne", plays="Espreita", lives="Florestas"),
    Animal(id=7, name="Coala", eats="Folhas de eucalipto", plays="Escalada", lives="Florestas"),
    Animal(id=8, name="Elefante", eats="Vegetação", plays="Banho de lama", lives="Savana"),
    Animal(id=9, name="Lobo", eats="Carne", plays="Caça em grupo", lives="Florestas"),
    Animal(id=10, name="Tartaruga", eats="Vegetação marinha", plays="Natação lenta", lives="Oceanos")
]

@router.get("/animals", response_model=list[Animal])
async def get_animals():
    return animals

@router.get("/animals/{animal_id}", response_model=Animal)
async def get_animal(animal_id: int):
    for animal in animals:
        if animal.id == animal_id:
            return animal
    raise HTTPException(status_code=404, detail="Animal não encontrado")
