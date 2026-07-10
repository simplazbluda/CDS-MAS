from backend.app.database.connection import engine
from backend.app.database.base import Base

from backend.app.database import models


print("Creating database tables...")

Base.metadata.create_all(
    bind=engine
)

print("Database tables created successfully!")