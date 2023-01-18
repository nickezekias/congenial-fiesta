from sqlalchemy import Boolean, Column, DateTime, Integer, JSON, String, Text

from src.app.db.base_class import Base
import uuid

class BusinessORM(Base):
    __tablename__ = "businesses"

    annual_turnover = Column(String, primary_key=True, nullable=True)
    business_model = Column(String, nullable=True)
    company_size = Column(String, nullable=False)
    company_type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    employees = Column(String, nullable=True) #remove nullable true
    id_document = Column(String, nullable=True)
    id_document_verified_at = Column(DateTime, nullable=True)
    industry = Column(String, nullable=False)
    investors = Column(String, nullable=True)
    locations = Column(String, nullable=True)
    markets = Column(String, nullable=True)
    name = Column(String, nullable=False)
    org_type = Column(String, nullable=False)
    partners = Column(String, nullable=True)
    payment = Column(String, nullable=True)
    payment_verified_at = Column(DateTime, nullable=True)
    pitch_deck = Column(String, nullable=True)
    products = Column(String, nullable=True)
    projects = Column(String, nullable=True)
    sector = Column(String, nullable=False)
    website = Column(Text, nullable=True)
    workspace = Column(JSON, nullable=False)
    year_founded = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def asdict(self):
        return {
            "id": self.id,
            "annual_turnover": self.annual_turnover,
            "business_model": self.business_model,
            "company_size": self.company_size,
            "company_type": self.company_type,
            "description": self.description,
            "employees": self.employees,
            "id_document": self.id_document,
            "id_document_verified_at": self.id_document_verified_at,
            "industry": self.industry,
            "investors": self.investors,
            "locations": self.locations,
            "markets": self.markets,
            "name": self.name,
            "org_type": self.org_type,
            "partners": self.partners,
            "payment": self.payment,
            "payment_verified_at": self.payment_verified_at,
            "pitch_deck": self.pitch_deck,
            "products": self.products,
            "projects": self.projects,
            "sector": self.sector,
            "website": self.website,
            "workspace": self.workspace,
            "year_founded": self.year_founded,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
