from enum import Enum

from Module_5.src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass

from Module_5.src.main.api.models.create_bank_account_response import CreateBankAccountResponse
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.create_user_response import CreateUserResponse
from Module_5.src.main.api.models.deposit_request import DepositRequest
from Module_5.src.main.api.models.deposit_response import DepositResponse
from Module_5.src.main.api.models.login_user_request import LoginUserRequest
from Module_5.src.main.api.models.login_user_response import LoginUserResponse
from Module_5.src.main.api.models.repay_credit_request import RepayCreditRequest
from Module_5.src.main.api.models.repay_credit_response import RepayCreditResponse
from Module_5.src.main.api.models.request_credit_request import RequestCreditRequest
from Module_5.src.main.api.models.request_credit_response import RequestCreditResponse
from Module_5.src.main.api.models.transfer_request import TransferRequest
from Module_5.src.main.api.models.transfer_response import TransferResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        url='admin/create',
        response_model=CreateUserResponse,
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        url='admin/users',
        response_model= None
    )

    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        url='auth/token/login',
        response_model=LoginUserResponse
    )

    CREATE_BANK_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url='account/create',
        response_model=CreateBankAccountResponse
    )

    DEPOSIT_BANK_ACCOUNT = EndpointConfiguration(
        request_model=DepositRequest,
        url='account/deposit',
        response_model=DepositResponse
    )

    TRANSFER_BANK_ACCOUNT = EndpointConfiguration(
        request_model=TransferRequest,
        url='account/transfer',
        response_model=TransferResponse
    )

    REQUEST_CREDIT = EndpointConfiguration(
        request_model=RequestCreditRequest,
        url='credit/request',
        response_model=RequestCreditResponse
    )

    REPAY_CREDIT = EndpointConfiguration(
        request_model=RepayCreditRequest,
        url='credit/repay',
        response_model=RepayCreditResponse
    )