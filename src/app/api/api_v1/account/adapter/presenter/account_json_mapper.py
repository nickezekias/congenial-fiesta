from src.domain.base.mapper import Mapper

from src.domain.account.user import User
from src.app.api.api_v1.account.adapter.request.register_request import UserPostRequest
from src.app.api.api_v1.account.adapter.response.user_response import UserPostResponse

from src.app.util.date_time_util import DateTimeUtil

class AccountJsonMapper(Mapper[UserPostRequest, User | UserPostResponse]):
    def mapToDomain(self, param: UserPostRequest) -> User:
        return User(
            id = "",
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = "",
            email_verified_at = None,
            phone_verified_at = None,
            ID_document = "",
            ID_document_verified_at = None,
            is_active = True,
            created_at = DateTimeUtil.string_to_date(param.created_at),
            updated_at = DateTimeUtil.string_to_date(param.updated_at)
        )

    def mapFromDomain(self, param: User) -> UserPostResponse:
        return UserPostResponse(
            id = param.id,
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = DateTimeUtil.date_to_iso_string(param.created_at),
            updated_at = DateTimeUtil.date_to_iso_string(param.updated_at)
        )