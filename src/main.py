from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.app.config.app import settings

from src.app.api.api_v1 import deps

#routers
from src.app.api.api_v1.account.routes import router as account_routes

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(account_routes)

@app.get("/")
async def root(db: Session = Depends(deps.get_db)):
    string = db.execute("SHOW TABLES").fetchall()
    return {"message": "Hello World", "db": string}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")