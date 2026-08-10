import pytest
from sqlalchemy.orm import Session

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.db.crud.account_crud import AccountCrudDb as Account
from Module_5.src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transfer
from Module_5.src.main.api.models.deposit_response import DepositResponse
from Module_5.src.main.api.models.two_accounts_deposited_response import TwoAccountsDeposited
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestTransferBankAccount:
    @pytest.mark.parametrize('amount',
                             [
                                 500, 5050.1, 10000
                             ], ids=['minimum', 'inside-range', 'maximum-and-full-balance'])
    def test_internal_transfer_valid(self, api_manager: ApiManager,
                                     user_with_two_accounts_deposited: TwoAccountsDeposited, amount: float,
                                     db_session: Session):
        response = api_manager.user_steps.first_transfers_second(user_with_two_accounts_deposited, amount)
        assert user_with_two_accounts_deposited.first_account.id == response.fromAccountId
        assert user_with_two_accounts_deposited.second_account.id == response.toAccountId
        assert response.fromAccountIdBalance == user_with_two_accounts_deposited.first_account.balance - amount

        db_session.expire_all()
        source_account = Account.get_account_by_id(db_session, response.fromAccountId)
        target_account = Account.get_account_by_id(db_session, response.toAccountId)
        assert source_account.balance == user_with_two_accounts_deposited.first_account.balance - amount
        assert target_account.balance == user_with_two_accounts_deposited.second_account.balance + amount

        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               user_with_two_accounts_deposited.first_account.id)
        assert transfer_from_db.from_account_id == response.fromAccountId
        assert transfer_from_db.to_account_id == response.toAccountId
        assert transfer_from_db.amount == amount

    @pytest.mark.parametrize('amount',
                             [
                                 500, 4500.99, 9000
                             ], ids=['minimum', 'inside-range', 'full-balance'])
    def test_external_transfer_valid(self, api_manager: ApiManager,
                                     two_users_with_accounts_deposited: TwoAccountsDeposited, amount: float,
                                     db_session: Session):
        response = api_manager.user_steps.first_transfers_second(two_users_with_accounts_deposited, amount)
        assert two_users_with_accounts_deposited.first_account.id == response.fromAccountId
        assert two_users_with_accounts_deposited.second_account.id == response.toAccountId
        assert response.fromAccountIdBalance == two_users_with_accounts_deposited.first_account.balance - amount

        db_session.expire_all()
        source_account = Account.get_account_by_id(db_session, response.fromAccountId)
        target_account = Account.get_account_by_id(db_session, response.toAccountId)
        assert source_account.balance == two_users_with_accounts_deposited.first_account.balance - amount
        assert target_account.balance == two_users_with_accounts_deposited.second_account.balance + amount

        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               two_users_with_accounts_deposited.first_account.id)
        assert transfer_from_db.from_account_id == response.fromAccountId
        assert transfer_from_db.to_account_id == response.toAccountId
        assert transfer_from_db.amount == amount

    @pytest.mark.parametrize('amount, exp_res',
                             [
                                 (-500, ResponseSpecs.request_bad()),
                                 (0, ResponseSpecs.request_bad()),
                                 (499.99, ResponseSpecs.request_bad()),
                                 (10000.01, ResponseSpecs.request_bad())
                             ], ids=['negative', 'zero', 'below-minimum', 'above-maximum'])
    def test_internal_transfer_invalid(self, api_manager: ApiManager,
                                       user_with_two_accounts_deposited: TwoAccountsDeposited, amount: float,
                                       exp_res: ResponseSpecs,
                                       db_session: Session):
        if amount > user_with_two_accounts_deposited.first_account.balance:
            api_manager.user_steps.deposit_bank(
                user_with_two_accounts_deposited,
                user_with_two_accounts_deposited.first_account.id,
                9000
            )

        api_manager.user_steps.first_transfers_second_invalid(user_with_two_accounts_deposited, amount,
                                                              exp_res)

        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               user_with_two_accounts_deposited.first_account.id)
        assert transfer_from_db is None

    @pytest.mark.parametrize('amount, exp_res',
                             [
                                 (-500, ResponseSpecs.request_bad()),
                                 (0, ResponseSpecs.request_bad()),
                                 (499.99, ResponseSpecs.request_bad()),
                                 (10000.01, ResponseSpecs.request_bad())
                             ], ids=['negative', 'zero', 'below-minimum', 'above-maximum'])
    def test_external_transfer_invalid(self, api_manager: ApiManager,
                                       two_users_with_accounts_deposited: TwoAccountsDeposited, amount: float,
                                       exp_res: ResponseSpecs,
                                       db_session: Session):
        if amount > two_users_with_accounts_deposited.first_account.balance:
            api_manager.user_steps.deposit_bank(
                two_users_with_accounts_deposited,
                two_users_with_accounts_deposited.first_account.id,
                9000
            )

        api_manager.user_steps.first_transfers_second_invalid(two_users_with_accounts_deposited, amount,
                                                              exp_res)

        transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                               two_users_with_accounts_deposited.first_account.id)
        assert transfer_from_db is None

    def test_transfer_more_than_balance_invalid(self, api_manager: ApiManager,
                                                user_with_two_accounts_empty: TwoAccountsEmpty,
                                                db_session: Session):
        deposited_account = api_manager.user_steps.deposit_bank(
            user_with_two_accounts_empty,
            user_with_two_accounts_empty.first_account.id,
            1000
        )
        accounts = TwoAccountsDeposited(
            first_account=deposited_account,
            second_account=DepositResponse(
                id=user_with_two_accounts_empty.second_account.id,
                balance=user_with_two_accounts_empty.second_account.balance
            ),
            user=user_with_two_accounts_empty.user
        )

        api_manager.user_steps.first_transfers_second_invalid(
            accounts,
            1000.01,
            ResponseSpecs.request_bad()
        )

        db_session.expire_all()
        source_account = Account.get_account_by_id(db_session, accounts.first_account.id)
        target_account = Account.get_account_by_id(db_session, accounts.second_account.id)
        assert source_account.balance == 1000
        assert target_account.balance == 0
        assert Transfer.get_transaction_by_from_id(db_session, accounts.first_account.id) is None

    def test_multiple_transfers_valid(self, api_manager: ApiManager,
                                      user_with_two_accounts_deposited: TwoAccountsDeposited,
                                      db_session: Session):
        transfer_amounts = [500, 1000, 2500.5]
        expected_source_balance = user_with_two_accounts_deposited.first_account.balance

        for amount in transfer_amounts:
            expected_source_balance -= amount
            response = api_manager.user_steps.first_transfers_second(
                user_with_two_accounts_deposited,
                amount
            )
            assert response.fromAccountIdBalance == expected_source_balance

        db_session.expire_all()
        source_account = Account.get_account_by_id(
            db_session,
            user_with_two_accounts_deposited.first_account.id
        )
        target_account = Account.get_account_by_id(
            db_session,
            user_with_two_accounts_deposited.second_account.id
        )
        transfers_from_db = Transfer.get_transactions_by_from_id(
            db_session,
            user_with_two_accounts_deposited.first_account.id
        )

        assert source_account.balance == expected_source_balance
        assert target_account.balance == (
            user_with_two_accounts_deposited.second_account.balance + sum(transfer_amounts)
        )
        assert [transfer.amount for transfer in transfers_from_db] == transfer_amounts
