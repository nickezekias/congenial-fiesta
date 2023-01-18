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
    annual_turnover: str
    business_model: str
    company_size: str | CompanySize
    company_type: str | CompanyType
    description: str
    employees: list
    ID_document: str
    ID_document_verified_at: str | None
    industry: Industry | str
    investors: list
    locations: list
    markets: list
    name: str
    org_type: OrgType | str
    partners: list
    payment: Payment | str | None
    payment_verified_at: str | None
    pitch_deck: bytes
    products: list
    projects: list
    sector: Sector | str
    website: str
    workspace: dict
    year_founded: str | None
    created_at: str
    updated_at: str