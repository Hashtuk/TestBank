import pytest
from sqlalchemy.orm import Session

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.db.crud.account_crud import AccountCrudDb as Account
from Module_5.src.main.api.db.crud.user_crud import UserCrudDb as User
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.two_accounts_empty_response import TwoAccountsEmpty
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestCreateBankAccount:
    def test_create_two_accounts_valid(self, api_manager: ApiManager,
                                       create_user: CreateUserRequest,
                                       db_session: Session):
        first_account = api_manager.user_steps.create_bank_account(create_user)
        second_account = api_manager.user_steps.create_bank_account(create_user)

        assert first_account.id != second_account.id
        assert first_account.number != second_account.number
        assert first_account.balance == 0
        assert second_account.balance == 0

        user_from_db = User.get_user_by_username(db_session, create_user.username)
        assert user_from_db is not None
        accounts_from_db = Account.get_accounts_by_user_id(db_session, user_from_db.id)

        assert [account.id for account in accounts_from_db] == [first_account.id, second_account.id]
        assert [account.number for account in accounts_from_db] == [first_account.number, second_account.number]
        assert all(account.balance == 0 for account in accounts_from_db)

    def test_create_third_account_invalid(self, api_manager: ApiManager,
                                          user_with_two_accounts_empty: TwoAccountsEmpty,
                                          db_session: Session):
        user_from_db = User.get_user_by_username(db_session, user_with_two_accounts_empty.user.username)
        assert user_from_db is not None
        accounts_before = Account.get_accounts_by_user_id(db_session, user_from_db.id)

        api_manager.user_steps.create_bank_account_invalid(
            user_with_two_accounts_empty.user,
            ResponseSpecs.request_bad()
        )

        db_session.expire_all()
        accounts_after = Account.get_accounts_by_user_id(db_session, user_from_db.id)
        assert len(accounts_before) == 2
        assert [account.id for account in accounts_after] == [account.id for account in accounts_before]
