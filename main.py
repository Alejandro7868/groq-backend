from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Lee el archivo .env y carga GROQ_API_KEY al entorno del sistema
load_dotenv()

# Crea la aplicación FastAPI (el "servidor")
app = FastAPI()

# Crea el cliente de Groq usando la API key cargada del .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define el molde de datos que debe recibir el endpoint
# Pydantic valida automáticamente que lleguen estos dos campos
class SolicitudUsuario(BaseModel):
    nombre: str
    prompt: str

# Endpoint POST en la ruta /chat
# Cuando alguien haga POST a /chat, se ejecuta esta función
@app.post("/chat")
def chat(solicitud: SolicitudUsuario):

    # Si alguno de los campos llega vacío, devuelve error 400
    if not solicitud.nombre or not solicitud.prompt:
        raise HTTPException(status_code=400, detail="Nombre y prompt son requeridos")

    # Llama a la API de Groq enviando el prompt como si fuera un mensaje de usuario
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Modelo gratuito de Groq
        messages=[
            {
                "role": "user",        # El rol indica quién habla (user = el usuario)
                "content": solicitud.prompt  # El contenido es el prompt recibido
            }
        ]
    )

    # De toda la respuesta de Groq, extraemos solo el texto generado
    texto_ia = respuesta.choices[0].message.content

    # Devolvemos un JSON con la respuesta personalizada
    return {
        "respuesta": f"{solicitud.nombre}, {texto_ia}"
    }