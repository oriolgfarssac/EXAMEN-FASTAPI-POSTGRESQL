from typing import Optional
import app
from MySQLdb import connect, Error
from fastapi import HTTPException
from pydantic import BaseModel

class Formulario(BaseModel):
    nombre: str
    apellido: str
    correo_electronico: str
    descripcion: Optional[str]
    curso: str
    ano: int
    direccion: str
    codigo_postal: Optional[int]
    password: str

async def add_user(item: Formulario) -> Optional[dict]:
    try:

        conn = connect(
            host="localhost",
            user="root",
            password="root",
            database="mydatabase"
        )

        cursor = conn.cursor()

        sql = """
        INSERT INTO Usuaris(nombre, apellido, correo_electronico,
        descripcion, curso, ano, direccion, codigo_postal, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            item.nombre, item.apellido, item.correo_electronico, item.descripcion,
            item.curso, item.ano, item.direccion, item.codigo_postal, item.password
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return {"nombre": item.nombre, "apellido": item.apellido}
    except Error as e:
        raise Exception(f"Error de base de datos: {str(e)}")

@app.post("/add_user/")
async def create_user(item: Formulario):
    try:
        user = await add_user(item)
        return {"mensaje": "El usuario se ha creado correctamente", "user": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
