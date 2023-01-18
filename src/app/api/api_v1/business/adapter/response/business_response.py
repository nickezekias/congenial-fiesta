from pydantic import BaseModel
from typing import TypeVar

from datetime import datetime
from src.domain.account.user import User

Industry = TypeVar('Industry')
Sector = TypeVar('Sector')
BusinessLocation = TypeVar('BusinessLocation')
BusinessMarket = TypeVar('BusinessMarket')
CompanySize = TypeVar('CompanySize')
CompanyType = TypeVar('CompanyType')
Business = TypeVar('Business')
Product = TypeVar('Product')
Project = TypeVar('Project')
Payment = TypeVar('Payment')
OrgType = TypeVar('OrgType')

class BusinessPostResponse(BaseModel):
    id: str
    annual_turnover: str | None
    business_model: bytes | None
    company_size: str | CompanySize
    company_type: str | CompanyType
    description: str
    employees: list[User] | None
    id_document: bytes | None
    id_document_verified_at: datetime | None
    industry: Industry | str
    investors: list[Business] | None
    locations: list[BusinessLocation] | None
    markets: list[BusinessMarket] | None
    name: str
    org_type: OrgType | str
    partners: list[Business] | None
    payment: Payment | str | None
    payment_verified_at: datetime | None
    pitch_deck: bytes | None
    products: list[Product] | str | None
    projects: list[Project] | str | None
    sector: Sector | str
    website: str | None
    workspace: dict
    year_founded: str | None
    created_at: str
    updated_at: str