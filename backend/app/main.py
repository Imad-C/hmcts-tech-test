import os
from dotenv import load_dotenv

from models import Base, Task
from schemas import TaskRead, TaskCreate

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()
app = FastAPI()

SQLALCHEMY_DATABASE_URL = f"{os.getenv('DATABASE_URI')}/{os.getenv('DATABASE_NAME')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.get('/health')
def route():
    return {"status": "ok"}

@app.get('/tasks', response_model = list[TaskRead])
def get_tasks(db: Session = Depends(get_db)): 
    tasks = db.query(Task).all()
    return tasks

@app.post('/tasks', response_model = TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)): 
    new_task = Task(**task.model_dump()) 
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
