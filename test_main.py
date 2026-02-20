from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_respuesta_exitosa():
    respuesta = client.post("/chat", json={
        "nombre": "Alejandro",
        "prompt": "¿Cuánto es 5 + 5?"
    })
    assert respuesta.status_code == 200, "El servidor debería responder con código 200"
    assert "Alejandro" in respuesta.json()["respuesta"], "La respuesta debería incluir el nombre del usuario"

def test_chat_nombre_vacio():
    respuesta = client.post("/chat", json={
        "nombre": "",
        "prompt": "¿Cuánto es 5 + 5?"
    })
    assert respuesta.status_code == 400, "Un nombre vacío debería retornar error 400"

def test_chat_prompt_vacio():
    respuesta = client.post("/chat", json={
        "nombre": "Alejandro",
        "prompt": ""
    })
    assert respuesta.status_code == 400, "Un prompt vacío debería retornar error 400"

def test_chat_campos_faltantes():
    respuesta = client.post("/chat", json={})
    assert respuesta.status_code == 422, "Campos faltantes deberían retornar error 422 de Pydantic"