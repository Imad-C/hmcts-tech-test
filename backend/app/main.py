import os
from dotenv import load_dotenv

from .models import Base, Task
from .schemas import TaskRead, TaskCreate

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()
app = FastAPI()

origins = [str(os.getenv('FRONTEND_URL_1')), str(os.getenv('FRONTEND_URL_2'))]
if any(origin == 'None' for origin in origins):
    raise KeyError("Missing FRONTEND_URL env variable.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.getenv('DATABASE_NAME')}"

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
