from dataclasses import dataclass
from datetime import datetime

from src.domain.base.entity import Entity
from src.domain.account.user import User
from src.domain.business.workspace import Workspace

from typing import TypeVar

Filter = TypeVar("Filter")

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

@dataclass
class Business(Entity):
    annual_turnover: str
    business_model: bytes
    company_size: str | CompanySize
    company_type: str | CompanyType
    description: str
    employees: list[User]
    ID_document: bytes
    ID_document_verified_at: datetime | None
    industry: Industry | str
    investors: list[Business]
    locations: list[BusinessLocation]
    markets: list[BusinessMarket]
    name: str
    org_type: OrgType | str
    partners: list[Business]
    payment: Payment | str
    payment_verified_at: datetime | None
    pitch_deck: bytes
    products: list[Product] | str
    projects: list[Project] | str
    sector: Sector | str
    website: str
    workspace: Workspace
    year_founded: datetime | None
    created_at: datetime
    updated_at: datetime
    id: str
    
    def __init__(
        self,
        id: str,
        annual_turnover: str,
        business_model: bytes,
        company_size: str | CompanySize,
        company_type: str | CompanyType,
        description: str,
        employees: list[User],
        ID_document: bytes,
        ID_document_verified_at: datetime | None,
        industry: Industry | str,
        investors: list[Business],
        locations: list[BusinessLocation],
        markets: list[BusinessMarket],
        name: str,
        org_type: OrgType | str,
        partners: list[Business],
        payment: Payment | str,
        payment_verified_at: datetime | None,
        pitch_deck: bytes,
        products: list[Product] | str,
        projects: list[Project] | str,
        sector: Sector | str,
        website: str,
        workspace: Workspace,
        year_founded: datetime | None,
        created_at: datetime,
        updated_at: datetime
    ) -> None:
        self.id = id
        self.annual_turnover = annual_turnover
        self.business_model = business_model
        self.company_size = company_size
        self.company_type = company_type
        self.description = description
        self.employees = employees
        self.ID_document = ID_document
        self.ID_document_verified_at = ID_document_verified_at
        self.industry = industry
        self.investors = investors
        self.locations = locations
        self.markets = markets
        self.name = name
        self.org_type = org_type
        self.partners = partners
        self.payment = payment
        self.payment_verified_at = payment_verified_at
        self.pitch_deck = pitch_deck
        self.products = products
        self.projects = projects
        self.sector = sector
        self.website = website
        self.workspace = workspace
        self.year_founded = year_founded
        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__()

    def get_partners(filter: Filter) -> list[Business]:
        pass

    def set_partners(partner: Business) -> None:
        pass

    def get_investors(filter: Filter) -> list[Business]:
        pass

    def set_investors(investor: Business) -> None:
        pass

    def add_location(location: BusinessLocation) -> None:
        pass

    def get_locations(filter: Filter) -> list[BusinessLocation]:
        pass

    def add_product(product: Product) -> None:
        pass

    def get_products(filter: Filter) -> list[Product]:
        pass

    def check_verification_status() -> bool:
        pass
