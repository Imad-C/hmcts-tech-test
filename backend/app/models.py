from sqlalchemy import Column, String, Integer, DateTime, Enum
from sqlalchemy.orm import declarative_base
from .utils import Status

Base = declarative_base()

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(Status), nullable=False)
    due = Column(DateTime, nullable=False)


