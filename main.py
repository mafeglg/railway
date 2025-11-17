from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.router import programas, usuarios, auth, grupos  # Agregar grupos
from app.router import cargar_archivos

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir en el objeto app los routers
app.include_router(usuarios.router, prefix="/usuario", tags=["servicios usuario"])
app.include_router(auth.router, prefix="/auth", tags=["servicios de login"])
app.include_router(cargar_archivos.router, prefix="/cargar", tags=["cargar archivos excel"])
app.include_router(programas.router)
app.include_router(grupos.router)  # NUEVO

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "ok",
        "autor": "ADSO 2925888 - Andres Jimenez M",
    }