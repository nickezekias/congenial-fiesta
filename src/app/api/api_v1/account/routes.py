from fastapi import APIRouter, Form, Depends
from datetime import timedelta
from datetime import datetime
from pydantic import EmailStr

from src.app.config.app import settings as app_settings
from src.app.api.api_v1.config.app import Settings
from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.business.i_business_repository import IBusinessRepository
from src.app.api.api_v1.account.adapter.request.login_request import LoginRequest
from src.app.api.api_v1.account.adapter.response.login_response import LoginResponse
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse
from src.app.api.api_v1.account.adapter.controller.login_controller import LoginController
from src.app.api.api_v1.account.adapter.controller.register_controller import RegisterController
from src.domain.account.i_account_presenter import IAccountPresenter
from src.app.api.api_v1.account.adapter.presenter.account_presenter import AccountPresenter
from src.app.api.api_v1.business.adapter.presenter.business_presenter import BusinessPresenter
from src.app.api.api_v1.account.adapter.presenter.register_presenter import RegisterPresenter

from src.app.api.api_v1.account.adapter.request.verify_email_request import VerifyEmailRequest
from src.app.api.api_v1.account.use_cases.verify_email import VerifyEmail as VerifyEmailUseCase

from src.domain.notification.i_notification import INotification
from src.app.api.api_v1.account.adapter.notification.forgot_password_notification import ForgotPasswordNotification
from src.app.api.api_v1.account.use_cases.forgot_password import ForgotPassword as ForgotPasswordUseCase

from src.app.api.api_v1.deps import get_settings
from src.app.api.api_v1.deps import get_account_mariadb_repository
from src.app.api.api_v1.deps import get_business_mariadb_repository
from src.app.api.api_v1.deps import get_authenticator

from src.app.util.crypto import Crypto

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

@router.post("/login", response_model=LoginResponse, status_code=200)
async def login(
    form_data: LoginRequest,
    settings: Settings = Depends(get_settings),
    repository: IAccountRepository = Depends(get_account_mariadb_repository),
    authenticator=Depends(get_authenticator)
) -> dict | None:
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    controller = LoginController(repository, authenticator)
    return await controller.login(form_data, access_token_expires)


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

@router.post("/verify-email", response_model=dict, status_code=200)
async def verify_email(
    payload: VerifyEmailRequest,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    presenter: IAccountPresenter = AccountPresenter()
    return await VerifyEmailUseCase(account_repository, presenter, Crypto).execute(payload)

@router.post("/forgot-password", response_model=dict, status_code=200)
async def forgot_password(
    email: EmailStr = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
) -> dict | None:
    notification: INotification = ForgotPasswordNotification()
    presenter: IAccountPresenter = AccountPresenter()
    return await ForgotPasswordUseCase(account_repository, presenter, Crypto, notification).execute(email)

    
