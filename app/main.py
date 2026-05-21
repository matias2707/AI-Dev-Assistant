from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers import root, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Dev Assistant")

app.include_router(root.router)
app.include_router(tasks.router)
