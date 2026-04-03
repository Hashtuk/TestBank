from Module_5.src.main.api.foundation.endpoint import Endpoint
from Module_5.src.main.api.foundation.requesters.crud_requester import CrudRequester
from Module_5.src.main.api.foundation.requesters.validated_crud_requester import ValidatedCrudRequester
from Module_5.src.main.api.models.account_with_credit_response import AccountWithCredit
from Module_5.src.main.api.models.create_bank_account_response import CreateBankAccountResponse
from Module_5.src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
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
from Module_5.src.main.api.models.two_accounts_deposited_response import TwoAccountsDeposited
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty
from Module_5.src.main.api.specs.request_specs import RequestSpecs
from Module_5.src.main.api.specs.response_specs import ResponseSpecs
from Module_5.src.main.api.steps.base_steps import BaseSteps
from typing import cast


class UserSteps(BaseSteps):
    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.unauth_headers(),
            endpoint=Endpoint.LOGIN_USER,
            response_spec=ResponseSpecs.request_ok()
        ).post(login_user_request)
        return cast(LoginUserResponse, response)

    def create_bank_account(self, create_user_request: CreateUserRequest):
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(create_user_request.username, create_user_request.password),
            endpoint=Endpoint.CREATE_BANK_ACCOUNT,
            response_spec=ResponseSpecs.request_created()
        ).post()
        return cast(CreateBankAccountResponse, response)

    def deposit_bank(self, two_accounts_empty: TwoAccountsEmpty, account_id, amount):
        deposit_request = DepositRequest(
            accountId=account_id,
            amount=amount
        )
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_empty.user.username,
                                                   two_accounts_empty.user.password),
            endpoint=Endpoint.DEPOSIT_BANK_ACCOUNT,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_request)
        return cast(DepositResponse, response)

    def deposit_bank_invalid(self, two_accounts_empty: TwoAccountsEmpty, account_id, amount,
                             expected_res: ResponseSpecs):
        deposit_request = DepositRequest(
            accountId=account_id,
            amount=amount
        )
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_empty.user.username,
                                                   two_accounts_empty.user.password),
            endpoint=Endpoint.DEPOSIT_BANK_ACCOUNT,
            response_spec=expected_res
        ).post(deposit_request)
        return response

    def first_transfers_second(self, two_accounts_deposited: TwoAccountsDeposited, amount):
        transfer_request = TransferRequest(
            fromAccountId=two_accounts_deposited.first_account.id,
            toAccountId=two_accounts_deposited.second_account.id,
            amount=amount
        )
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_deposited.user.username,
                                                   two_accounts_deposited.user.password),
            endpoint=Endpoint.TRANSFER_BANK_ACCOUNT,
            response_spec=ResponseSpecs.request_ok()
        ).post(transfer_request)
        return cast(TransferResponse, response)

    def first_transfers_second_invalid(self, two_accounts_deposited: TwoAccountsDeposited, amount,
                                       expected_res: ResponseSpecs):
        transfer_request = TransferRequest(
            fromAccountId=two_accounts_deposited.first_account.id,
            toAccountId=two_accounts_deposited.second_account.id,
            amount=amount
        )
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_deposited.user.username,
                                                   two_accounts_deposited.user.password),
            endpoint=Endpoint.TRANSFER_BANK_ACCOUNT,
            response_spec=expected_res
        ).post(transfer_request)
        return response

    def request_credit(self, two_accounts_empty: TwoAccountsEmpty,
                       amount, months):
        credit_request = RequestCreditRequest(
            accountId=two_accounts_empty.first_account.id,
            amount=amount,
            termMonths=months
        )
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_empty.user.username,
                                                   two_accounts_empty.user.password),
            endpoint=Endpoint.REQUEST_CREDIT,
            response_spec=ResponseSpecs.request_created()
        ).post(credit_request)
        return cast(RequestCreditResponse, response)

    def request_credit_invalid(self, two_accounts_empty: TwoAccountsEmpty,
                       amount, months, expected_res: ResponseSpecs):
        credit_request = RequestCreditRequest(
            accountId=two_accounts_empty.first_account.id,
            amount=amount,
            termMonths=months
        )
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(two_accounts_empty.user.username,
                                                   two_accounts_empty.user.password),
            endpoint=Endpoint.REQUEST_CREDIT,
            response_spec=expected_res
        ).post(credit_request)
        return response

    def repay_credit(self, account_with_credit: AccountWithCredit):
        repay_credit_request = RepayCreditRequest(
            creditId=account_with_credit.credit_response.creditId,
            accountId=account_with_credit.credit_response.id,
            amount=account_with_credit.credit_response.amount
        )
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(account_with_credit.user.username,
                                                   account_with_credit.user.password),
            endpoint=Endpoint.REPAY_CREDIT,
            response_spec=ResponseSpecs.request_ok()
        ).post(repay_credit_request)
        return cast(RepayCreditResponse, response)

    def repay_credit_invalid(self, account_with_credit: AccountWithCredit, amount, expected_res: ResponseSpecs):
        repay_credit_request = RepayCreditRequest(
            creditId=account_with_credit.credit_response.creditId,
            accountId=account_with_credit.credit_response.id,
            amount=amount
        )
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(account_with_credit.user.username,
                                                   account_with_credit.user.password),
            endpoint=Endpoint.REPAY_CREDIT,
            response_spec=expected_res
        ).post(repay_credit_request)
        return response
