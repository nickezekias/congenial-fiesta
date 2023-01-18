from fastapi import APIRouter, Depends

from src.app.api.api_v1.business.adapter.request.business_request import BusinessPostRequest
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse

from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.business.i_business_presenter import IBusinessPresenter


router = APIRouter(
    tag=["business"]
)

@router.post("/", response_model=BusinessPostResponse)
async def create(form: BusinessPostRequest):
    pass