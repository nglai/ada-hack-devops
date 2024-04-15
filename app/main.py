from fastapi import FastAPI
from .routes.animal import router as animal_router

app = FastAPI()

# Inclui as rotas dos animais
app.include_router(animal_router)

# Rota inicial
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Consulta sobre Animais de um Zoo"}
