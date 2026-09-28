from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine, get_db
from models import Laptop

LAPTOPS_INICIALES = [
    {"marca": "Dell", "modelo": "Latitude 5440", "ram_gb": 16, "disponible": True},
    {"marca": "Lenovo", "modelo": "ThinkPad E14", "ram_gb": 8, "disponible": False},
    {"marca": "HP", "modelo": "ProBook 450", "ram_gb": 16, "disponible": True},
]


class LaptopCreate(BaseModel):
    marca: str
    modelo: str
    ram_gb: int


class LaptopResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    marca: str
    modelo: str
    ram_gb: int
    disponible: bool


def cargar_datos_iniciales(db):
    if db.query(Laptop).count() == 0:
        for datos in LAPTOPS_INICIALES:
            db.add(Laptop(**datos))
        db.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        cargar_datos_iniciales(db)
    finally:
        db.close()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def raiz():
    return {"mensaje": "API del laboratorio de cómputo"}


@app.get("/laptops", response_model=list[LaptopResponse])
def listar_laptops(db: Session = Depends(get_db)):
    return db.query(Laptop).order_by(Laptop.id).all()


@app.get("/laptops/disponibles", response_model=list[LaptopResponse])
def listar_disponibles(db: Session = Depends(get_db)):
    return db.query(Laptop).filter(Laptop.disponible == True).order_by(Laptop.id).all()


@app.get("/laptops/{laptop_id}", response_model=LaptopResponse)
def obtener_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.id == laptop_id).first()
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return laptop


@app.post("/laptops", response_model=LaptopResponse)
def crear_laptop(datos: LaptopCreate, db: Session = Depends(get_db)):
    laptop = Laptop(
        marca=datos.marca,
        modelo=datos.modelo,
        ram_gb=datos.ram_gb,
        disponible=True,
    )
    db.add(laptop)
    db.commit()
    db.refresh(laptop)
    return laptop
