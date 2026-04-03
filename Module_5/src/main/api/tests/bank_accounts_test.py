import pytest
from Module_5.src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transfer
from Module_5.src.main.api.db.crud.account_crud import AccountCrudDb as Account
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestDepositBankAccount:
    @pytest.mark.parametrize('amount',
                             [
                                 1000, 4500.1, 9000
                             ])
    def test_deposit_valid(self, api_manager, user_with_two_accounts_empty, amount, db_session):
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
    def test_deposit_invalid(self, api_manager, user_with_two_accounts_empty, amount, exp_res, db_session):
        api_manager.user_steps.deposit_bank_invalid(user_with_two_accounts_empty,
                                                    user_with_two_accounts_empty.first_account.id, amount,
                                                    exp_res)

        account_from_db = Account.get_account_by_id(db_session, user_with_two_accounts_empty.first_account.id)
        assert account_from_db.balance == user_with_two_accounts_empty.first_account.balance

    @pytest.mark.api
    class TestTransferBankAccount:
        @pytest.mark.parametrize('amount',
                                 [
                                     500, 5050.1, 10000
                                 ])
        def test_internal_transfer_valid(self, api_manager, user_with_two_accounts_deposited, amount, db_session):
            response = api_manager.user_steps.first_transfers_second(user_with_two_accounts_deposited, amount)
            assert user_with_two_accounts_deposited.first_account.id == response.fromAccountId
            assert user_with_two_accounts_deposited.second_account.id == response.toAccountId
            assert response.fromAccountIdBalance == user_with_two_accounts_deposited.first_account.balance - amount

            transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                                   user_with_two_accounts_deposited.first_account.id)
            assert transfer_from_db.from_account_id == response.fromAccountId
            assert transfer_from_db.to_account_id == response.toAccountId
            assert transfer_from_db.amount == amount

        @pytest.mark.parametrize('amount',
                                 [
                                     500.1, 4500.99, 8999.9
                                 ])
        def test_external_transfer_valid(self, api_manager, two_users_with_accounts_deposited, amount, db_session):
            response = api_manager.user_steps.first_transfers_second(two_users_with_accounts_deposited, amount)
            assert two_users_with_accounts_deposited.first_account.id == response.fromAccountId
            assert two_users_with_accounts_deposited.second_account.id == response.toAccountId
            assert response.fromAccountIdBalance == two_users_with_accounts_deposited.first_account.balance - amount

            transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                                   two_users_with_accounts_deposited.first_account.id)
            assert transfer_from_db.from_account_id == response.fromAccountId
            assert transfer_from_db.to_account_id == response.toAccountId
            assert transfer_from_db.amount == amount

        @pytest.mark.parametrize('amount, exp_res',
                                 [
                                     (499.5, ResponseSpecs.request_bad()),
                                     (10001, ResponseSpecs.request_bad())
                                 ])
        def test_internal_transfer_invalid(self, api_manager, user_with_two_accounts_deposited, amount, exp_res,
                                           db_session):
            api_manager.user_steps.first_transfers_second_invalid(user_with_two_accounts_deposited, amount,
                                                                  exp_res)

            transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                                   user_with_two_accounts_deposited.first_account.id)
            assert transfer_from_db is None

        @pytest.mark.parametrize('amount, exp_res',
                                 [
                                     (499.5, ResponseSpecs.request_bad()),
                                     (10001, ResponseSpecs.request_bad())
                                 ])
        def test_external_transfer_invalid(self, api_manager, two_users_with_accounts_deposited, amount, exp_res,
                                           db_session):
            api_manager.user_steps.first_transfers_second_invalid(two_users_with_accounts_deposited, amount,
                                                                  exp_res)

            transfer_from_db = Transfer.get_transaction_by_from_id(db_session,
                                                                   two_users_with_accounts_deposited.first_account.id)
            assert transfer_from_db is None
