"""
Database Connection
-------------------

Creates the SQLAlchemy engine and session
for the MedicalAI SQLite database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file
DATABASE_URL = "sqlite:///./medical_ai.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    FastAPI dependency for database sessions.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()