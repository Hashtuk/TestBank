from sqlalchemy.orm import Session
from Module_5.src.main.api.db.models.account_table import Account


class AccountCrudDb:
    @staticmethod
    def get_account_by_id(db: Session, account_id: int) -> Account | None:
        return db.query(Account).filter_by(id=account_id).first()

    @staticmethod
    def get_accounts_by_user_id(db: Session, user_id: int) -> list[Account]:
        return db.query(Account).filter_by(user_id=user_id).order_by(Account.id).all()
