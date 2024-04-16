
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API de Consulta sobre Animais"}

@pytest.mark.asyncio
async def test_get_animals():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/animals")
    assert response.status_code == 200
    animals = response.json()
    assert isinstance(animals, list)
    assert len(animals) == 10  # Verifica se há 10 animais na lista

@pytest.mark.asyncio
async def test_get_specific_animal():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/animals/1")
    assert response.status_code == 200
    animal = response.json()
    assert animal["id"] == 1
    assert animal["name"] == "Leão"

@pytest.mark.asyncio
async def test_get_animal_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/animals/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Animal não encontrado"}