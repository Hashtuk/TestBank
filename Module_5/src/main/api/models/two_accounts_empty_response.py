from Module_5.src.main.api.models.base_model import BaseModel
from Module_5.src.main.api.models.create_bank_account_response import CreateBankAccountResponse
from Module_5.src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from Module_5.src.main.api.models.create_user_request import CreateUserRequest


class TwoAccountsEmpty(BaseModel):
    first_account: CreateBankAccountResponse
    second_account: CreateBankAccountResponse
    user: CreateUserRequest | CreateCreditUserRequest