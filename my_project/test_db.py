from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/mydb"

print(repr(DATABASE_URL))

engine = create_engine(DATABASE_URL)

conn = engine.connect()
print("OK")
conn.close()