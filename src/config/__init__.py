import os


# from .env import (
#     POSTGRESQL_HOST,
#     POSTGRESQL_PORT,
#     POSTGRESQL_DBNAME,
#     DB_USER,
#     DB_PASS
# )

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#####################################################################
# postgresql

POSTGRESQL_HOST = '127.0.0.1'
POSTGRESQL_PORT = '5432'
POSTGRESQL_DBNAME = 'testdb'
DB_USER = 'postgres'
DB_PASS = '12345qwe'
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DBNAME}"
