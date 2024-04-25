from typing import Union
from fastapi import FastAPI, HTTPException, status
from database import engine, Base, ToDo
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI, version


Base.metadata.create_all(engine)
import shemas

app = FastAPI()

origins = ["*"]
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_methods=["*"],
allow_headers=["*"],


)

@app.get("/")

def read_root():
    return "TODO app"

@app.post("/dodaj", status_code=status.HTTP_201_CREATED)
@version(1)
def dodaj_todo(todo:shemas.ToDo):
    session = Session(bind=engine,expire_on_commit=False)
    todoDB = ToDo(task =todo.task)
    session.add(todoDB)
    session.commit()
    id = todoDB.id
    session.close()
    return f"Nov ToDo id {id}"

@app.delete("/delete/{id}")
def delete_todo(id:int):
    return "delete ToDo"

@app.put("/update/{id}")
def update_todo():
    return "update ToDo"

@app.get("/get/{id}")
def get_todo():
    return "get ToDo"

app = VersionedFastAPI(app,version_format='{major}', prefix_format="/v{major}")