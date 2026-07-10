from sqlalchemy import inspect

from backend.app.database.connection import engine


inspector = inspect(engine)

print(
    inspector.get_table_names()
)