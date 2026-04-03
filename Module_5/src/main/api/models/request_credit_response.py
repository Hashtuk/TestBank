from Module_5.src.main.api.models.base_model import BaseModel


class RequestCreditResponse(BaseModel):
    id: int # в сваггере поле accountId?
    amount: float
    termMonths: int
    balance: float
    creditId: int