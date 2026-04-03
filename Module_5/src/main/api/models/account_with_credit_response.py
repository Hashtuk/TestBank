from Module_5.src.main.api.models.base_model import BaseModel
from Module_5.src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from Module_5.src.main.api.models.request_credit_response import RequestCreditResponse


class AccountWithCredit(BaseModel):
    credit_response: RequestCreditResponse
    user: CreateCreditUserRequest