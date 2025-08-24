from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, crud

app = FastAPI(title="ChakraV Backend")

# create tables on startup
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "Welcome to ChakraV POC 🚀"}

@app.post("/users/")
def create_user(name: str, db: Session = Depends(database.get_db)):
    user = crud.create_user(db=db, name=name)
    return user

@app.get("/users/")
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db=db)
