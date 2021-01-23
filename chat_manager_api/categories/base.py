from chat_manager_api.abc import BaseAPICategoryABC, ChatManagerAPIABC


class BaseAPICategory(BaseAPICategoryABC):

    def __init__(self, api: "ChatManagerAPIABC"):
        self.api = api
