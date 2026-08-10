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
                             ], ids=['minimum', 'inside-range', 'maximum'])
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
                                 (-1000, ResponseSpecs.request_bad()),
                                 (0, ResponseSpecs.request_bad()),
                                 (999.99, ResponseSpecs.request_bad()),
                                 (9000.01, ResponseSpecs.request_bad())
                             ], ids=['negative', 'zero', 'below-minimum', 'above-maximum'])
    def test_deposit_invalid(self, api_manager: ApiManager, user_with_two_accounts_empty: TwoAccountsEmpty,
                             amount: float, exp_res: ResponseSpecs, db_session: Session):
        api_manager.user_steps.deposit_bank_invalid(user_with_two_accounts_empty,
                                                    user_with_two_accounts_empty.first_account.id, amount,
                                                    exp_res)

        account_from_db = Account.get_account_by_id(db_session, user_with_two_accounts_empty.first_account.id)
        assert account_from_db.balance == user_with_two_accounts_empty.first_account.balance

    def test_multiple_deposits_valid(self, api_manager: ApiManager,
                                     user_with_two_accounts_empty: TwoAccountsEmpty,
                                     db_session: Session):
        account_id = user_with_two_accounts_empty.first_account.id
        expected_balance = user_with_two_accounts_empty.first_account.balance

        for amount in [1000, 9000, 2500.5]:
            expected_balance += amount
            response = api_manager.user_steps.deposit_bank(
                user_with_two_accounts_empty,
                account_id,
                amount
            )
            assert response.balance == expected_balance

        db_session.expire_all()
        account_from_db = Account.get_account_by_id(db_session, account_id)
        assert account_from_db.balance == expected_balance
