from sqlalchemy.orm import Session
from Module_5.src.main.api.db.models.transaction_table import Transaction

class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_from_id(db: Session, from_account_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(from_account_id=from_account_id).first()

    @staticmethod
    def get_transactions_by_from_id(db: Session, from_account_id: int) -> list[Transaction]:
        return db.query(Transaction).filter_by(from_account_id=from_account_id).order_by(Transaction.id).all()
