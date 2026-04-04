import pytest
from sqlalchemy.orm import Session

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from Module_5.src.main.api.models.account_with_credit_response import AccountWithCredit
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty
from Module_5.src.main.api.specs.response_specs import ResponseSpecs
from Module_5.src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transfer


@pytest.mark.api
class TestBankCredit:
    @pytest.mark.parametrize(
        'amount, months', [
            (5000, 1),
            (15000, 12)
        ]
    )
    def test_request_credit_valid(self, api_manager: ApiManager, credit_user_with_two_accounts_empty: TwoAccountsEmpty,
                                  amount: float,
                                  months: int, db_session: Session):
        response = api_manager.user_steps.request_credit(credit_user_with_two_accounts_empty,
                                                         amount,
                                                         months)
        assert credit_user_with_two_accounts_empty.first_account.id == response.id
        assert response.amount == amount
        assert response.balance == credit_user_with_two_accounts_empty.first_account.balance + amount
        assert response.termMonths == months

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.account_id == credit_user_with_two_accounts_empty.first_account.id
        assert credit_from_db.id == response.creditId
        assert credit_from_db.amount == amount
        assert credit_from_db.term_months == months

    def test_repay_credit_valid(self, api_manager: ApiManager, credit_user_with_credit: AccountWithCredit,
                                db_session: Session):
        response = api_manager.user_steps.repay_credit(credit_user_with_credit)
        assert response.creditId == credit_user_with_credit.credit_response.creditId
        assert response.amountDeposited == credit_user_with_credit.credit_response.amount

        credit_from_db = Credit.get_credit_by_id(db_session, credit_user_with_credit.credit_response.creditId)
        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               credit_user_with_credit.credit_response.id)
        assert credit_from_db.balance == 0
        assert transfer_from_db.amount == credit_user_with_credit.credit_response.amount

    @pytest.mark.parametrize(
        'amount, months, exp_res', [
            (4999.9, 1, ResponseSpecs.request_bad()),
            (15000.5, 12, ResponseSpecs.request_bad()),  # Приходит 400, вместо 422?
            (10000, 61, ResponseSpecs.request_bad()),
            (10000, 0, ResponseSpecs.request_bad())
        ]
    )
    def test_request_credit_invalid(self, api_manager: ApiManager,
                                    credit_user_with_two_accounts_empty: TwoAccountsEmpty, amount: float,
                                    months: int, exp_res: ResponseSpecs, db_session: Session):
        api_manager.user_steps.request_credit_invalid(credit_user_with_two_accounts_empty,
                                                      amount,
                                                      months, exp_res)

        credit_from_db = Credit.get_credit_by_account_id(db_session,
                                                         credit_user_with_two_accounts_empty.first_account.id)
        assert credit_from_db is None

    @pytest.mark.parametrize(
        'amount, exp_res', [
            (9999.9, ResponseSpecs.request_unprocessable()),
            (10000.5, ResponseSpecs.request_unprocessable()),
            (-10000, ResponseSpecs.request_bad())
        ]
    )
    def test_repay_credit_invalid(self, api_manager: ApiManager, credit_user_with_credit: AccountWithCredit,
                                  amount: float, exp_res: ResponseSpecs, db_session: Session):
        api_manager.user_steps.repay_credit_invalid(credit_user_with_credit, amount, exp_res)

        credit_from_db = Credit.get_credit_by_id(db_session, credit_user_with_credit.credit_response.creditId)
        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               credit_user_with_credit.credit_response.id)
        assert transfer_from_db is None
        assert credit_from_db.amount == credit_user_with_credit.credit_response.amount
