from database import Base, engine
import models  # важно, чтобы User загрузился

Base.metadata.create_all(bind=engine)

print("TABLES CREATED")