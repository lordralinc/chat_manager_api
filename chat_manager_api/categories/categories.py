from chat_manager_api.abc import APICategoriesABC
from .account import AccountAPICategory


class APICategories(APICategoriesABC):

    @property
    def account(self) -> AccountAPICategory:
        return AccountAPICategory(self.api_instance)
