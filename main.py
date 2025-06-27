from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simula base de datos
items = []

# Modelo de datos
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: str = ""

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡API funcionando correctamente!"}


# Crear un item
@app.post("/items")
def crear_item(item: Item):
    for i in items:
        if i.id == item.id:
            raise HTTPException(status_code=400, detail="ID ya existe")
    items.append(item)
    return item

# Leer todos los items
@app.get("/items")
def listar_items():
    return items

# Leer un item por ID
@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

# Actualizar un item
@app.put("/items/{item_id}")
def actualizar_item(item_id: int, item_actualizado: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = item_actualizado
            return item_actualizado
    raise HTTPException(status_code=404, detail="Item no encontrado")

# Eliminar un item
@app.delete("/items/{item_id}")
def eliminar_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return {"mensaje": "Item eliminado"}
    raise HTTPException(status_code=404, detail="Item no encontrado")
