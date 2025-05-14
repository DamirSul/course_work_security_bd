# main.py

from fastapi import FastAPI
from app.database import engine
from app.models import Base

# Импортируем маршруты
from app.endpoints import routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ИС по выращиванию цветов")

for router, prefix, tag in routes:
    app.include_router(router, prefix=prefix, tags=[tag])
