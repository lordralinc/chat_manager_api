from pydantic import BaseModel


class GetWebHookInfo(BaseModel):
    id: int
    url: str
    last_request: int
    last_status: int
    last_fail: int
    fails: int


SetWebHook = GetWebHookInfo
