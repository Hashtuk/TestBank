import pytest
from sqlalchemy.orm import Session

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.db.crud.account_crud import AccountCrudDb as Account
from Module_5.src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from Module_5.src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transfer
from Module_5.src.main.api.db.crud.user_crud import UserCrudDb as User
from Module_5.src.main.api.generators.model_generator import RandomModelGenerator
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.two_accounts_deposited_response import TwoAccountsDeposited
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestAdminUser:
    @pytest.mark.parametrize(
        'username_length, password',
        [
            (3, 'ABCd12!$_!'),
            (15, 'ABCd12!$_!'),
            (8, 'Aa1!aaaa'),
            (8, 'Aa1!$_aa')
        ],
        ids=['username-min', 'username-max', 'password-min', 'password-with-allowed-specials']
    )
    def test_create_user_valid(self, api_manager: ApiManager, username_length: int,
                               password: str, db_session: Session):
        request = CreateUserRequest(
            username=RandomModelGenerator.generate_alphanumeric(username_length),
            password=password,
            role='ROLE_USER'
        )

        response = api_manager.admin_steps.create_user(request)

        assert response.username == request.username
        assert response.role == request.role

        user_from_db = User.get_user_by_username(db_session, request.username)
        assert user_from_db is not None
        assert user_from_db.id == response.id
        assert user_from_db.username == request.username
        assert user_from_db.role == request.role

    @pytest.mark.parametrize(
        'username, password',
        [
            (RandomModelGenerator.generate_alphanumeric(2), 'Aa1!aaaa'),
            (RandomModelGenerator.generate_alphanumeric(16), 'Aa1!aaaa'),
            (f'{RandomModelGenerator.generate_alphanumeric(7)}_', 'Aa1!aaaa'),
            (f'{RandomModelGenerator.generate_alphanumeric(3)}!', 'Aa1!aaaa'),
            ('абв', 'Aa1!aaaa'),
            (RandomModelGenerator.generate_alphanumeric(8), 'Aa1!aaa'),
            (RandomModelGenerator.generate_alphanumeric(8), 'aa1!aaaa'),
            (RandomModelGenerator.generate_alphanumeric(8), 'AA1!AAAA'),
            (RandomModelGenerator.generate_alphanumeric(8), 'Aaa!aaaa'),
            (RandomModelGenerator.generate_alphanumeric(8), 'Aa11aaaa'),
            (RandomModelGenerator.generate_alphanumeric(8), 'Aa1!аааа')
        ],
        ids=[
            'username-below-minimum',
            'username-above-maximum',
            'username-with-underscore',
            'username-with-special',
            'username-cyrillic',
            'password-below-minimum',
            'password-without-uppercase',
            'password-without-lowercase',
            'password-without-digit',
            'password-without-special',
            'password-cyrillic'
        ]
    )
    def test_create_user_invalid(self, api_manager: ApiManager, username: str,
                                 password: str, db_session: Session):
        request = CreateUserRequest(
            username=username,
            password=password,
            role='ROLE_USER'
        )

        api_manager.admin_steps.create_user_invalid(
            request,
            ResponseSpecs.request_bad()
        )

        assert User.get_user_by_username(db_session, username) is None

    def test_soft_delete_user_preserves_related_data(
            self, api_manager: ApiManager,
            credit_user_with_credit_and_transfer: TwoAccountsDeposited,
            db_session: Session):
        user_from_db = User.get_user_by_username(
            db_session,
            credit_user_with_credit_and_transfer.user.username
        )
        assert user_from_db is not None

        api_manager.admin_steps.delete_user(user_from_db.id)

        db_session.expire_all()
        deleted_user_from_db = User.get_user_by_username(
            db_session,
            credit_user_with_credit_and_transfer.user.username
        )
        accounts_after = Account.get_accounts_by_user_id(db_session, user_from_db.id)
        credit_after = Credit.get_credit_by_account_id(
            db_session,
            credit_user_with_credit_and_transfer.first_account.id
        )
        transactions_after = Transfer.get_transactions_by_from_id(
            db_session,
            credit_user_with_credit_and_transfer.first_account.id
        )

        assert deleted_user_from_db is not None
        assert deleted_user_from_db.deleted_at is not None
        assert [account.id for account in accounts_after] == [
            credit_user_with_credit_and_transfer.first_account.id,
            credit_user_with_credit_and_transfer.second_account.id
        ]
        assert [account.balance for account in accounts_after] == [
            credit_user_with_credit_and_transfer.first_account.balance,
            credit_user_with_credit_and_transfer.second_account.balance
        ]
        assert credit_after is not None
        assert credit_after.account_id == credit_user_with_credit_and_transfer.first_account.id
        assert credit_after.amount == 10000
        assert credit_after.term_months == 6
        assert transactions_after
        assert transactions_after[-1].from_account_id == credit_user_with_credit_and_transfer.first_account.id
        assert transactions_after[-1].to_account_id == credit_user_with_credit_and_transfer.second_account.id
        assert transactions_after[-1].amount == 500
