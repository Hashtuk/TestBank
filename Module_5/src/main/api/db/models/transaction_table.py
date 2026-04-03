from sqlalchemy import Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from Module_5.src.main.api.db.base import Base
from datetime import datetime


class Transaction(Base):
    __tablename__ = 'transaction'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    to_account_id: Mapped[int] = mapped_column(Integer, ForeignKey('account.id'))
    from_account_id: Mapped[int] = mapped_column(Integer, ForeignKey('account.id'))
    credit_id: Mapped[int] = mapped_column(Integer, ForeignKey('credit.id'))
    amount: Mapped[float] = mapped_column(Float)
    transaction_type: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime | None] = mapped_column(DateTime)

    def __repr__(self):
        return (f'<Transaction(id={self.id}, '
                f'to_account_id={self.to_account_id}, '
                f'from_account_id={self.from_account_id}, '
                f'credit_id={self.credit_id}, '
                f'amount={self.amount}, '
                f'transaction_type={self.transaction_type}, '
                f'created_at={self.created_at})>')
