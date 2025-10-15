import os
from sqlalchemy import create_engine
from models import Base, SpamControl, ServerConfig, WorkTime
import database

def init_db():
    print("Starting database initialization...")
    
    # Delete old database if exists
    print("Checking for existing database...")
    if os.path.exists('database.db'):
        print("Removing old database...")
        os.remove('database.db')
    
    print("Creating tables...")
    database.init_db()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()