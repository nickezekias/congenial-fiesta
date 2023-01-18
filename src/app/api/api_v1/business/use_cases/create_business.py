from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.base.i_use_case import IUseCase
from src.domain.business.i_business_presenter import IBusinessPresenter

from src.domain.business.business import Business

class CreateBusiness(IUseCase):
    repository: IBusinessRepository
    presenter: IBusinessPresenter

    def __init__(self, repository: IBusinessRepository, presenter: IBusinessPresenter) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, business: Business) -> Business:
        business: Business = self.repository.add(entity=business, NO_COMMIT=True)
        return self.presenter.output(business)
