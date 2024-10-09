import uvicorn
from fastapi import FastAPI, status, HTTPException
from typing import List

from starlette.middleware.cors import CORSMiddleware

from src.models import ToDo
from src.database import Database

description = """
Simple backend api for CRUD operations for ToDo project

## Operations
You can list all tasks in the todo list, but also insert and remove a single task.

* list: returns all tasks in todo list
* insert: adds a new document to the database collection
* delete: removes a single document from the collection

## Database
MongoDB
## Database name
* ticketing
## Collection
* tickets

"""

origins = [
    "http://localhost",
    "https://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8080",
]

app = FastAPI(
    title='ToDo Api',
    description=description
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


database = Database()


@app.get("/todos", response_model=List[ToDo])
async def list_all():
    return database.list_all()


@app.delete("/todos/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    try:
        database.delete(id)
    except:
        raise HTTPException(status_code=404, detail="This 'todo' was not found")


@app.post("/todos/insert", response_model=ToDo, status_code=status.HTTP_201_CREATED)
async def insert(todo: ToDo) -> ToDo:
    inserted = database.insert(todo)
    if inserted is None:
        raise HTTPException(status_code=404, detail="This 'todo' couldn't be saved")

    return inserted


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
