from fastapi import FastAPI, status, File, UploadFile, HTTPException, Form
from decouple import config 
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

url = config("SUPABASE_URL")
key = config("SUPABASE_KEY")

app = FastAPI()
supabase: Client = create_client(url, key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DocumentosSchema(BaseModel):
    Nombre: str
    Descripción: Optional[str] = None

@app.get("/documentos/")
def get_documento():
    documento = supabase.table("documentos").select("*").execute()
    if hasattr(documento, "error") and documento.error:
        raise HTTPException(status_code=500, detail=documento.error.message)
    return documento.data if hasattr(documento, "data") else documento

@app.post("/documento/", status_code=status.HTTP_201_CREATED)
async def create_documento(
    Nombre: str = Form(...),
    Descripción: Optional[str] = Form(None),
    archivo: UploadFile = File(...)
):
    try:
        contenido_archivo = await archivo.read()
        nombre_archivo = f"{Nombre}_{datetime.now().isoformat()}"
        bucket_name = "documentos"
        
        # Subir archivo al bucket
        storage_response = supabase.storage.from_(bucket_name).upload(
            nombre_archivo, contenido_archivo
        )

        if hasattr(storage_response, "error") and storage_response.error:
            raise HTTPException(status_code=500, detail=storage_response.error.message)

        # Generar URL pública del archivo
        public_url = supabase.storage.from_(bucket_name).get_public_url(nombre_archivo)

        # Guardar metadatos en la tabla
        response = supabase.table("documentos").insert({
            "tipo": "archivo",
            "nombre": Nombre,
            "descripción": Descripción,
            "url": public_url,  # Guardar la URL pública
            "fecha_creación": datetime.now().isoformat()
        }).execute()

        if hasattr(response, "error") and response.error:
            raise HTTPException(status_code=500, detail=response.error.message)
        
        return {"message": "Documento subido exitosamente", "data": response.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/documentos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documento(id: str):
    documento = supabase.table("documentos").select("*").eq("id", id).execute()
    if hasattr(documento, "data") and not documento.data:
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    # Borrar archivo del bucket
    delete_storage_response = supabase.storage.from_("documentos").remove([documento.data[0]["url"]])
    
    if hasattr(delete_storage_response, "error") and delete_storage_response.error:
        raise HTTPException(status_code=500, detail=delete_storage_response.error.message)

    # Eliminar metadatos de la base de datos
    delete_response = supabase.table("documentos").delete().eq("id", id).execute()
    if hasattr(delete_response, "error") and delete_response.error:
        raise HTTPException(status_code=500, detail=delete_response.error.message)

    return {"message": "Documento eliminado con éxito"}

@app.put("/documento/{id}", status_code=status.HTTP_200_OK)
async def update_documento(
    id: str,
    Nombre: str = Form(...),
    Descripción: Optional[str] = Form(None),
):
    try:
        response = supabase.table("documentos").update({
            "nombre": Nombre,
            "descripción": Descripción,
            "fecha_creación": datetime.now().isoformat()
        }).eq("id", id).execute()

        if hasattr(response, "error") and response.error:
            raise HTTPException(status_code=500, detail=response.error.message)

        return {"message": "Documento actualizado exitosamente", "data": response.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))