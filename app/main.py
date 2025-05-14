# main.py

from fastapi import FastAPI
from app.database import engine
from app.models import Base

# Импортируем маршруты
from app.endpoints import routes

from app.models import Resource
from app.database import SessionLocal

def init_resources():
    db = SessionLocal()
    defaults = [
        {"id": 1, "resource_name": "Удобрения"},
        {"id": 2, "resource_name": "Средства защиты"},
        {"id": 3, "resource_name": "Доп средства"},
    ]

    for res in defaults:
        exists = db.query(Resource).filter_by(id=res["id"]).first()
        if not exists:
            db.add(Resource(id=res["id"], resource_name=res["resource_name"], quantity_available=0))
    db.commit()
    db.close()


Base.metadata.create_all(bind=engine)
init_resources()  # <-- ДОБАВЬ ЭТО

app = FastAPI(title="ИС по выращиванию цветов")

for router, prefix, tag in routes:
    app.include_router(router, prefix=prefix, tags=[tag])
