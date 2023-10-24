from pydantic import BaseModel, validator
from datetime import datetime
from src.app.util.date_time_util import DateTimeUtil
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
    
    @validator('year_founded')
    def date_string_must_be_valid(cls, v):
        try:
            if v != datetime.strptime(v, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S'):
                raise ValueError("forms.errors.invalid.invalidDateString")
            return v
        except ValueError:
            raise ValueError("forms.errors.invalid.invalidDateString")
