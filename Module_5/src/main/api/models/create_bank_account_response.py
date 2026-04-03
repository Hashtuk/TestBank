from Module_5.src.main.api.models.base_model import BaseModel


class CreateBankAccountResponse(BaseModel):
    id: int
    number: str
    balance: float