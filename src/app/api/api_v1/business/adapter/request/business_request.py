from pydantic import BaseModel
class BusinessPostRequest(BaseModel):
    id: str = ""
    company_size: str
    company_type: str
    description: str
    industry: str
    name: str
    org_type: str
    sector: str
    website: str
    workspace: dict
    year_founded: str | None
    created_at: str
    updated_at: str