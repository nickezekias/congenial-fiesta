from fastapi import APIRouter, Depends
from dataclasses import asdict
import sqlalchemy as sa
from sqlalchemy.orm import Session
from src.app.api.api_v1.deps import get_db
from src.app.db.session import engine
from typing import Any

router = APIRouter(
    tags=["ext-api"]
)

metadata = sa.MetaData()

CompanyTypeORM = sa.Table("company_types", metadata, autoload_with=engine)
IndustryORM = sa.Table('industries', metadata, autoload_with=engine)
OrgTypeORM = sa.Table("organization_types", metadata, autoload_with=engine)
SectorORM = sa.Table("sectors", metadata, autoload_with=engine)

@router.get("/company-types", response_model=Any)
async def index(db: Session = Depends(get_db)):
    res = db.query(CompanyTypeORM).order_by("name").all()
    return res

@router.get("/industries", response_model=Any)
async def index(db: Session = Depends(get_db)):
    res = db.query(IndustryORM).order_by("name").all()
    # res = db.execute(sa.select(IndustryORM).where(1 == 1)).fetchall()
    return res

@router.get("/org-types", response_model=Any)
async def index(db: Session = Depends(get_db)):
    res = db.query(OrgTypeORM).order_by("name").all()
    return res

@router.get("/sectors", response_model=Any)
async def index(db: Session = Depends(get_db)):
    res = db.query(SectorORM).order_by("name").all()
    return res