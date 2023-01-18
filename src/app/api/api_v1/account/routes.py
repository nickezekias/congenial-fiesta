from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.app.api.api_v1.account.adapter.controller.login_controller import LoginController
from src.app.api.api_v1.account.adapter.controller.register_controller import RegisterController

from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.presenter.register_presenter import RegisterPresenter


from src.domain.business.i_business_repository import IBusinessRepository

from src.app.api.api_v1.business.adapter.presenter.business_presenter import BusinessPresenter
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

from src.app.api.api_v1.deps import get_account_mariadb_repository
from src.app.api.api_v1.deps import get_business_mariadb_repository
from src.app.api.api_v1.deps import get_authenticator

from src.domain.account.user import User
from typing import Any
from datetime import datetime

router = APIRouter(
    tags=["auth"]
)


@router.get("/", response_model=RegisterResponse, status_code=200)
async def index():
    # return [{"id": 1, "avatar": "me.jpg", "first_name": "Ezekiel", "last_name": "Madu",  "email": "maduezekiel@example.com", "phone": "9838282", "is_active": True}]
    user = User(
        id = "",
        avatar = "me.jpg",
        first_name = "Nick",
        last_name = "Arts",
        email = "nickezekias@gmail.com",
        phone = "077848483",
        password = "password",
        password_confirmation = "password",
        token = None,
        email_verified_at = None,
        phone_verified_at = None,
        ID_document = None,
        ID_document_verified_at = None,
        is_active = True,
        created_at = datetime.strptime("2022-11-11:01:12:22", '%Y-%m-%d:%H:%M:%S'),
        updated_at = datetime.strptime("2022-11-11:00:00:00", '%Y-%m-%d:%H:%M:%S')
    )
    business = {
        "id": "d898fd",
        "company_size": "1 - 5",
        "company_type": "private",
        "description": "Lorem ipsum",
        "industry": "Energy",
        "name": "Energia",
        "org_type": "company",
        "sector": "Energy Distribution",
        "website": "energia.example.com",
        "workspace": {
            "id": "83923823",
            "currency": "usd",
            "timezone": "GMT+1",
            "time_format": "24H",
            "date_format": "yyyy-mm-dd"
        },
        "year_founded": "1986-11-11:00:00:00",
        "created_at": "2022-11-11:00:00:00",
        "updated_at": "2022-11-11:00:00:00"
    }
    return RegisterPresenter().output(user, business_res=business)

@router.post("/login", response_model=dict, status_code=200)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), repository: IAccountRepository = Depends(get_account_mariadb_repository), authenticator=Depends(get_authenticator)) -> dict | None:
    controller = LoginController(repository, authenticator)
    return await controller.login(form_data)


@router.post("/register", response_model=RegisterResponse, status_code=201)
async def register(
    form_data: RegisterRequest,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
    business_repository: IBusinessRepository = Depends(get_business_mariadb_repository),
    authenticator=Depends(get_authenticator
)) -> RegisterResponse | None:
    controller = RegisterController(
        account_repository,
        RegisterPresenter(),
        business_repository,
        BusinessPresenter(),
        authenticator
    )
    return await controller.register(form_data)
