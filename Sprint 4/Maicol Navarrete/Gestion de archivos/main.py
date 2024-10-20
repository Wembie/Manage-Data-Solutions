from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from models import Base, engine, SessionLocal, File as FileModel
import shutil
import os

app = FastAPI()

# Ruta para guardar los archivos subidos
UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Dependencia de la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para subir un archivo
@app.post("/upload/", summary="Subir un archivo", description="Sube un archivo y guarda sus metadatos en la base de datos.")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"{UPLOAD_DIR}{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    file_size = os.path.getsize(file_location)
    
    # Verificar si el archivo ya existe
    db_file = db.query(FileModel).filter(FileModel.filename == file.filename).first()
    if db_file:
        raise HTTPException(status_code=400, detail="File already exists")
    
    # Guardar los metadatos en la base de datos
    file_record = FileModel(
        filename=file.filename,
        content_type=file.content_type,
        size=file_size,
        path=file_location
    )
    
    db.add(file_record)
    db.commit()
    db.refresh(file_record)
    
    return {
        "id": file_record.id,
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file_size,
        "path": file_location
    }

# Endpoint para listar todos los archivos
@app.get("/files/", summary="Listar archivos", description="Lista todos los archivos disponibles en la base de datos.")
async def list_files(db: Session = Depends(get_db)):
    files = db.query(FileModel).all()
    return [
        {
            "id": file.id,
            "filename": file.filename,
            "content_type": file.content_type,
            "size": file.size,
            "path": file.path
        } for file in files
    ]

# Endpoint para obtener los detalles de un archivo específico por ID
@app.get("/files/{file_id}", summary="Obtener detalles de un archivo", description="Obtiene los metadatos de un archivo específico a partir de su ID.")
async def get_file_details(file_id: int, db: Session = Depends(get_db)):
    file = db.query(FileModel).filter(FileModel.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return {
        "id": file.id,
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size,
        "path": file.path
    }

# Endpoint para eliminar un archivo por ID
@app.delete("/files/{file_id}", summary="Eliminar un archivo", description="Elimina un archivo y sus metadatos de la base de datos.")
async def delete_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(FileModel).filter(FileModel.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    # Eliminar el archivo del sistema de archivos
    if os.path.exists(file.path):
        os.remove(file.path)
    
    # Eliminar los metadatos de la base de datos
    db.delete(file)
    db.commit()
    
    return {"detail": "File deleted successfully"}