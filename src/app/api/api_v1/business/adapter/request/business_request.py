from pydantic import BaseModel
from typing import TypeVar
from src.domain.business.workspace import Workspace

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

class BusinessPostRequest(BaseModel):
    id: str = ""
    company_size: str | CompanySize
    company_type: str | CompanyType
    description: str
    industry: Industry | str
    name: str
    org_type: OrgType | str
    sector: Sector | str
    website: str | None
    workspace: Workspace
    year_founded: str | None
    created_at: str
    updated_at: str