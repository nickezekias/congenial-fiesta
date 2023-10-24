from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from src.app.config.app import settings

from src.app.api.api_v1 import deps

#routers
from src.app.api.api_v1.account.routes import router as account_routes
from src.app.api.api_v1.ext_api.routes import router as ext_api_routes

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_routes, prefix="/api/v1")
app.include_router(ext_api_routes, prefix="/api/v1")

@app.get("/")
async def root(db: Session = Depends(deps.get_db)):
    string = db.execute("SHOW TABLES").fetchall()
    return {"message": "Hello World", "db": string}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")