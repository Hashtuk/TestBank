from Module_5.src.main.api.models.base_model import BaseModel
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.deposit_response import DepositResponse


class TwoAccountsDeposited(BaseModel):
    first_account: DepositResponse
    second_account: DepositResponse
    user: CreateUserRequest