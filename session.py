from sqlalchemy.orm import Session
from database import get_session

_session = None

def get_db() -> Session:
    """Get the current database session"""
    global _session
    if _session is None:
        _session = get_session()
    return _session

def close_db():
    """Close the current database session"""
    global _session
    if _session is not None:
        _session.close()
        _session = None