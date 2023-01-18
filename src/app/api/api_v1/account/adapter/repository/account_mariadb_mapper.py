from src.domain.base.mapper import Mapper
from src.domain.account.user import User
from src.app.db.models.user_orm import UserORM

class AccountMariaDbMapper(Mapper[UserORM, User]):
    def mapToDomain(self, param: UserORM) -> User:
        user =  User(
            id = param.id,
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = param.token,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = param.created_at,
            updated_at = param.updated_at,
        )
        return user
        

    def mapToDomainList(self, params: list[UserORM]) -> list[UserORM]:
        users: list[User]
        for param in params:
            users.append(self.mapToDomain(param))
        return users

    def mapFromDomain(self, param: User) -> UserORM:
        return UserORM(
            id=param.id,
            avatar=param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = param.token,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = param.created_at,
            updated_at = param.updated_at,
        )

    def mapFromDomainList(self, params: list[User]) -> list[UserORM]:
        orms: list[UserORM]
        for param in params:
            orms.append(self.mapFromDomain(param))
        return orms
