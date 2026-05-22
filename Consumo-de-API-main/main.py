# pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Evento(BaseModel):
    id: int
    nome: str
    palestrante: str

banco_eventos: List[Evento] = []

@app.get("/eventos")
def listar_eventos():
    return banco_eventos

@app.post("/eventos")
def criar_evento(evento: Evento):
    banco_eventos.append(evento)
    return evento

@app.put("/eventos/{evento_id}")
def atualizar_evento(evento_id: int, evento: Evento):
    for index, event in enumerate(banco_eventos):
        if event.id == evento_id:
            banco_eventos[index] = evento
            return evento
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@app.delete("/eventos/{evento_id}")
def remover_evento(evento_id: int):
    for index, event in enumerate(banco_eventos):
        if event.id == evento_id:
            banco_eventos.pop(index)
            return {"message": "Evento removido com sucesso"}
    raise HTTPException(status_code=404, detail="Evento não encontrado")



    #python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
    #-m: procura dentro das bibliotecas no python
    #unicorn: é o servidor web em si
    #main: esse arquivo
    #app: nome que foi dado a api na linha 7
    #--reload: salva o código quando em execução, e reinicia sozinho
    #--host 0.0.0.0: aceita qualquer máquina externa na mesma rede

    #port 8000: porta TCP, que direciona para o unicorn
