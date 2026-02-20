from fastapi.testclient import TestClient
from main import app

# Crea un cliente de prueba que simula peticiones a tu API
client = TestClient(app)

def test_chat_respuesta_exitosa():
    respuesta = client.post("/chat", json={
        "nombre": "Alejandro",
        "prompt": "¿Cuánto es 5 + 5?"
    })
    assert respuesta.status_code == 200
    assert "Alejandro" in respuesta.json()["respuesta"]

def test_chat_nombre_vacio():
    respuesta = client.post("/chat", json={
        "nombre": "",
        "prompt": "¿Cuánto es 5 + 5?"
    })
    assert respuesta.status_code == 400

def test_chat_prompt_vacio():
    respuesta = client.post("/chat", json={
        "nombre": "Alejandro",
        "prompt": ""
    })
    assert respuesta.status_code == 400

def test_chat_campos_faltantes():
    respuesta = client.post("/chat", json={})
    assert respuesta.status_code == 422