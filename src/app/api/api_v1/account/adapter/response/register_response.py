from pydantic import BaseModel

from src.app.api.api_v1.account.adapter.response.user_response import UserPostResponse
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse

class RegisterResponse(BaseModel):
    user: UserPostResponse
    business: BusinessPostResponse