from chat_manager_api.categories.base import BaseAPICategory
from chat_manager_api.models import account


class AccountAPICategory(BaseAPICategory):

    def get_web_hook_info(self) -> account.GetWebHookInfo:
        return self.api.make_request("account.getWebHookInfo", dataclass=account.GetWebHookInfo)

    async def get_web_hook_info_async(self) -> account.GetWebHookInfo:
        return await self.api.make_request_async("account.getWebHookInfo", dataclass=account.GetWebHookInfo)

    def set_web_hook(self, url: str) -> account.SetWebHook:
        return self.api.make_request("account.setWebHook", data=dict(url=url), dataclass=account.SetWebHook)

    async def set_web_hook_async(self, url: str) -> account.SetWebHook:
        return await self.api.make_request_async("account.setWebHook", data=dict(url=url), dataclass=account.SetWebHook)

    def remove_web_hook(self) -> str:
        return self.api.make_request("account.removeWebHook", dataclass=str)

    async def remove_web_hook_async(self) -> str:
        return await self.api.make_request_async("account.removeWebHook", dataclass=str)
