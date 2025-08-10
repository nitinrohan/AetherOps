# Line 1: Import FastAPI to create our web application
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .db import engine  # uses settings.DATABASE_URL from .env

# Line 4: Create an app instance that Uvicorn will serve
app = FastAPI(title="AetherOps API", version="0.1.0")

# Line 7: Simple health endpoint for uptime checks (no DB required yet)
@app.get("/health")
async def health():
    # Line 10: If this returns {"status":"ok"}, the API process is alive
    return {"status": "ok"}
@app.get("/db/ping")
async def db_ping():
    """
    Connectivity check: run SELECT 1 on MySQL.
    """
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            return {"db": "ok", "result": result.scalar()}
    except SQLAlchemyError as e:
        return {"db": "error", "detail": str(e)}