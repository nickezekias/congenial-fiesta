from pydantic import BaseModel
from src.app.api.api_v1.account.adapter.request.user_request import UserPostRequest
from src.app.api.api_v1.business.adapter.request.business_request import BusinessPostRequest

class RegisterRequest(BaseModel):
    user: UserPostRequest
    business: BusinessPostRequest