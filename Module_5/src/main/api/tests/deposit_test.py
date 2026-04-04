import pytest
from sqlalchemy.orm import Session

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.db.crud.account_crud import AccountCrudDb as Account
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestDepositBankAccount:
    @pytest.mark.parametrize('amount',
                             [
                                 1000, 4500.1, 9000
                             ])
    def test_deposit_valid(self, api_manager: ApiManager, user_with_two_accounts_empty: TwoAccountsEmpty, amount: float,
                           db_session: Session):
        response = api_manager.user_steps.deposit_bank(user_with_two_accounts_empty,
                                                       user_with_two_accounts_empty.first_account.id, amount)
        assert user_with_two_accounts_empty.first_account.id == response.id
        assert amount == response.balance

        account_from_db = Account.get_account_by_id(db_session, user_with_two_accounts_empty.first_account.id)
        assert account_from_db.id == response.id
        assert account_from_db.balance == response.balance

    @pytest.mark.parametrize('amount, exp_res',
                             [
                                 (999.9, ResponseSpecs.request_bad()),
                                 (9001, ResponseSpecs.request_bad())
                             ])
    def test_deposit_invalid(self, api_manager: ApiManager, user_with_two_accounts_empty: TwoAccountsEmpty,
                             amount: float, exp_res: ResponseSpecs, db_session: Session):
        api_manager.user_steps.deposit_bank_invalid(user_with_two_accounts_empty,
                                                    user_with_two_accounts_empty.first_account.id, amount,
                                                    exp_res)

        account_from_db = Account.get_account_by_id(db_session, user_with_two_accounts_empty.first_account.id)
        assert account_from_db.balance == user_with_two_accounts_empty.first_account.balance
