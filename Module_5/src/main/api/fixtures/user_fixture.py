import pytest

from Module_5.src.main.api.generators.model_generator import RandomModelGenerator
from Module_5.src.main.api.models.account_with_credit_response import AccountWithCredit
from Module_5.src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.two_accounts_deposited_response import TwoAccountsDeposited
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty



@pytest.fixture
def create_user(api_manager):
    request = RandomModelGenerator.generate(CreateUserRequest)
    response = api_manager.admin_steps.create_user(request)
    return request


@pytest.fixture
def create_credit_user(api_manager):
    request = RandomModelGenerator.generate(CreateCreditUserRequest)
    response = api_manager.admin_steps.create_user(request)
    return request


@pytest.fixture
def user_with_two_accounts_empty(api_manager, create_user):
    first_account = api_manager.user_steps.create_bank_account(create_user)
    second_account = api_manager.user_steps.create_bank_account(create_user)
    creds = TwoAccountsEmpty(
        first_account=first_account,
        second_account=second_account,
        user=create_user
    )
    return creds

@pytest.fixture
def credit_user_with_two_accounts_empty(api_manager, create_credit_user):
    first_account = api_manager.user_steps.create_bank_account(create_credit_user)
    second_account = api_manager.user_steps.create_bank_account(create_credit_user)
    creds = TwoAccountsEmpty(
        first_account=first_account,
        second_account=second_account,
        user=create_credit_user
    )
    return creds


@pytest.fixture
def user_with_two_accounts_deposited(api_manager, user_with_two_accounts_empty):
    api_manager.user_steps.deposit_bank(user_with_two_accounts_empty, user_with_two_accounts_empty.first_account.id,
                                        1000)
    first_account = api_manager.user_steps.deposit_bank(user_with_two_accounts_empty,
                                                        user_with_two_accounts_empty.first_account.id,
                                                        9000)
    second_account = api_manager.user_steps.deposit_bank(user_with_two_accounts_empty,
                                                         user_with_two_accounts_empty.second_account.id,
                                                         5000)
    creds = TwoAccountsDeposited(
        first_account=first_account,
        second_account=second_account,
        user=user_with_two_accounts_empty.user
    )
    return creds


@pytest.fixture
def two_users_with_accounts_deposited(api_manager):
    first_user = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(first_user)
    second_user = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(second_user)
    first_user_account_one = api_manager.user_steps.create_bank_account(first_user)
    first_user_account_two = api_manager.user_steps.create_bank_account(first_user)
    second_user_account_one = api_manager.user_steps.create_bank_account(second_user)
    second_user_account_two = api_manager.user_steps.create_bank_account(second_user)
    first_creds = TwoAccountsEmpty(
        first_account=first_user_account_one,
        second_account=first_user_account_two,
        user=first_user
    )
    second_creds = TwoAccountsEmpty(
        first_account=second_user_account_one,
        second_account=second_user_account_two,
        user=second_user
    )
    first_account_deposited = api_manager.user_steps.deposit_bank(first_creds, first_creds.first_account.id, 9000)
    second_account_deposited = api_manager.user_steps.deposit_bank(second_creds, second_creds.first_account.id, 9000)

    creds = TwoAccountsDeposited(
        first_account=first_account_deposited,
        second_account=second_account_deposited,
        user=first_user
    )
    return creds

@pytest.fixture
def credit_user_with_credit(api_manager, credit_user_with_two_accounts_empty):
    credit = api_manager.user_steps.request_credit(credit_user_with_two_accounts_empty, 10000, 6)

    creds = AccountWithCredit(
        credit_response=credit,
        user=credit_user_with_two_accounts_empty.user
    )
    return creds


