from fastapi import FastAPI
from schemas import AvaliacaoDisplay, ErrorResponse, AvaliacaoBase

app = FastAPI()

@app.post("/formulario_avaliacao", responses={"200": AvaliacaoDisplay, "400": ErrorResponse})
def responder_formulario_avaliacao(formulario: AvaliacaoBase):
    pass

