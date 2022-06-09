from typing import Optional
from pydantic import BaseModel


class TelegramResponseParameters(BaseModel):
    retry_after: int


class TelegramResponse(BaseModel):
    ok: bool
    error_code: Optional[int]
    description: Optional[str]
    paramters: Optional[TelegramResponseParameters]
