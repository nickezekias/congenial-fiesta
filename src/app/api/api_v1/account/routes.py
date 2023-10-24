from fastapi import APIRouter, BackgroundTasks, Form, Depends
from datetime import timedelta
from datetime import datetime
from pydantic import EmailStr
from typing import Annotated

from typing import Any
from src.app.config.app import settings as app_settings
from src.app.api.api_v1.config.app import Settings
from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_register_presenter import IRegisterPresenter
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
from src.app.api.api_v1.account.adapter.notification.verify_email_notification import VerifyEmailNotification

from src.app.api.api_v1.account.adapter.request.verify_email_request import VerifyEmailRequest
from src.app.api.api_v1.account.use_cases.verify_email import VerifyEmail as VerifyEmailUseCase

from src.domain.notification.notification import Notification
from src.app.api.api_v1.account.adapter.notification.forgot_password_notification import ForgotPasswordNotification
from src.app.api.api_v1.account.use_cases.forgot_password import ForgotPassword as ForgotPasswordUseCase

from src.app.api.api_v1.account.use_cases.reset_password import ResetPassword as ResetPasswordUseCase

from src.app.api.api_v1.deps import get_settings
from src.app.api.api_v1.deps import get_account_mariadb_repository
from src.app.api.api_v1.deps import get_business_mariadb_repository
from src.app.api.api_v1.deps import get_authenticator

from src.app.util.crypto import Crypto

router = APIRouter(
    tags=["auth"]
)

#TODO: REMOVE THIS UNUSED ROUTE
@router.post("/test", response_model=Any)
async def test(background_tasks: BackgroundTasks):
    token = Crypto.generate_token("nickezekias@gmail.com", "minutes", 60)
    token_2 = Crypto.generate_token("nickezekias@gmail.com", "minutes", 60)

    manual_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjM3Njc0NDc5MzY2LjczNDgyLCJuYmYiOjE2NzQ0ODI5NjYsInN1YiI6Im5pY2tlemVraWFzQGdtYWlsLmNvbSJ9.-DsuVbgqmIpkLc0bc0S1HzKiqs_6AgXuQ7B6QVMBKrk"

    res = Crypto.verify_token(token)

    user = User(
        id = "",
        avatar = "me.jpg",
        first_name = "Nick",
        last_name = "Arts",
        email = "nickezekias@gmail.com",
        phone = "077848483",
        password = "password",
        # password_confirmation = "password",
        token = None,
        email_verified_at = None,
        phone_verified_at = None,
        ID_document = None,
        ID_document_verified_at = None,
        is_active = True,
        created_at = datetime.strptime("2022-11-11:01:12:22", '%Y-%m-%d:%H:%M:%S'),
        updated_at = datetime.strptime("2022-11-11:00:00:00", '%Y-%m-%d:%H:%M:%S')
    )

    # notification: Notification = ForgotPasswordNotification()
    # notification.notifiable = user
    # notification.token = token
    # await notification.send()
    # background_tasks.add_task(notification.send)
    comp = token == token_2
    return {"detail": "Making sure 2 generated tokens with the same subjects are different",  "token_1": token, "token_2": token_2, "comp": comp, "res": res }


#TODO: REMOVE THIS UNUSED ROUTE
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
        # password_confirmation = "password",
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


@router.post("/register", response_model=Any, status_code=201)
async def register(
    form_data: RegisterRequest,
    background_tasks: BackgroundTasks,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
    business_repository: IBusinessRepository = Depends(get_business_mariadb_repository),
    authenticator=Depends(get_authenticator)
) -> Any | None:
    notification: Notification = VerifyEmailNotification(background_tasks)
    controller = RegisterController(
        account_repository,
        RegisterPresenter(),
        business_repository,
        BusinessPresenter(),
        authenticator,
        notification,
        crypto=Crypto
    )
    return await controller.register(form_data)

@router.post("/verify-email", response_model=dict, status_code=200)
async def verify_email(
    payload: VerifyEmailRequest,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    presenter: IAccountPresenter = AccountPresenter()
    return await VerifyEmailUseCase(account_repository, presenter, Crypto).execute(payload)

# check no user with same email exists
@router.post("/check-email-unicity", response_model=dict, status_code=200)
async def check_email(
    email: str = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    found_user: User = account_repository.get_by_email(email = email)
    if found_user:
        return { "success": False, "detail": "app.account.register.errors.emailExists" }
    else: return { "success": True, "detail": "app.account.register.success.emailIsUnique" }

# check no user with same phone exists
@router.post("/check-phone-unicity", response_model=dict, status_code=200)
async def check_phone(
    phone: str = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    found_user: User = account_repository.get_by_phone(phone = phone)
    # return { "phone": phone }
    if found_user:
        return { "success": False, "detail": "app.account.register.errors.phoneExists" }
    else: return { "success": True, "detail": "app.account.register.success.phoneIsUnique" }
    

@router.post("/forgot-password", response_model=dict, status_code=200)
async def forgot_password(
    background_tasks: BackgroundTasks,
    email: EmailStr = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
) -> dict | None:
    notification: Notification = ForgotPasswordNotification(background_tasks)
    presenter: IAccountPresenter = AccountPresenter()
    return await ForgotPasswordUseCase(account_repository, presenter, Crypto, notification).execute(email)

@router.post("/reset-password", response_model=dict, status_code=200)
async def reset_password(
    payload: ResetPasswordUseCase.Request,
    repository: IAccountRepository = Depends(get_account_mariadb_repository),
    authenticator = Depends(get_authenticator)
) -> dict:
    presenter: IAccountPresenter = AccountPresenter()
    return await ResetPasswordUseCase(
        repository=repository,
        presenter=presenter,
        crypto=Crypto,
        authenticator=authenticator
    ).execute(payload)


    
