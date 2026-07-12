from backend.app.database.base import Base
from backend.app.database.connection import engine

# Import models so SQLAlchemy registers tables
from backend.app.database import models


def init_database():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    init_database()

    print(
        "Database initialized successfully"
    )