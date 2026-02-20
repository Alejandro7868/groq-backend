from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SolicitudUsuario(BaseModel):
    nombre: str
    prompt: str

#endpoint que sirve el archivo HTML
@app.get("/")
def index():
    return FileResponse("index.html")

@app.post("/chat")
def chat(solicitud: SolicitudUsuario):
    if not solicitud.nombre or not solicitud.prompt:
        raise HTTPException(status_code=400, detail="Nombre y prompt son requeridos")

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": solicitud.prompt
            }
        ]
    )

    texto_ia = respuesta.choices[0].message.content

    return {
        "respuesta": f"{solicitud.nombre}, {texto_ia}"
    }