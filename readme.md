# Groq Backend

API REST desarrollada con FastAPI que funciona como intermediario entre el usuario y la API de inteligencia artificial de Groq.

## ¿Qué hace?

Recibe el nombre de un usuario y una pregunta, consulta a la IA de Groq y devuelve una respuesta personalizada. Por ejemplo, si el usuario se llama Alejandro y pregunta "¿Cuánto es 5 + 5?", el servicio responde: "Alejandro, la respuesta es 10".

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- Groq API (modelo llama-3.3-70b-versatile)
- Uvicorn
- Pydantic
- python-dotenv

## Requisitos previos

- Python 3.10 o superior
- Una API Key de Groq (puede obtenerse gratis en https://console.groq.com)

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/Alejandro7868/groq-backend.git
cd groq-backend
```

2. Crear y activar el entorno virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

4. Crear el archivo `.env` en la raíz del proyecto con la API Key
```
GROQ_API_KEY=tu_clave_aqui
```

## Uso

1. Iniciar el servidor
```bash
python -m uvicorn main:app --reload
```

2. Abrir el navegador en
```
http://127.0.0.1:8000
```

3. Escribir nombre y pregunta en la interfaz y hacer clic en Enviar

## Endpoint disponible

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | / | Sirve la interfaz HTML |
| POST | /chat | Recibe nombre y prompt, devuelve respuesta personalizada |

## Ejemplo de petición
```json
POST /chat
{
  "nombre": "Alejandro",
  "prompt": "¿Cuánto es 5 + 5?"
}
```

## Ejemplo de respuesta
```json
{
  "respuesta": "Alejandro, la respuesta es 10."
}
```

## Pruebas unitarias
```bash
pytest test_main.py -v
```

## Estructura del proyecto
```
groq-backend/
├── main.py           → lógica principal del backend
├── index.html        → interfaz de usuario
├── requirements.txt  → dependencias del proyecto
├── .env              → API Key (no se sube a GitHub)
├── .gitignore        → archivos ignorados por Git
└── test_main.py      → pruebas unitarias
```