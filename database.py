from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
from typing import Optional
import os

_engine: Optional[Engine] = None
_Session: Optional[sessionmaker] = None

def get_engine() -> Engine:
    """Get SQLAlchemy engine, creating it if needed"""
    global _engine
    if _engine is None:
        db_path = os.path.join(os.path.dirname(__file__), 'attendance.db')
        _engine = create_engine(f'sqlite:///{db_path}')
    return _engine

def get_session_factory() -> sessionmaker:
    """Get SQLAlchemy session factory, creating it if needed"""
    global _Session
    if _Session is None:
        _Session = sessionmaker(bind=get_engine())
    return _Session

def init_db():
    """Initialize the database, creating all tables"""
    Base.metadata.create_all(get_engine())

def get_session() -> Session:
    """Get a new database session"""
    return get_session_factory()()