from sqlalchemy import Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from Module_5.src.main.api.db.base import Base
from datetime import datetime


class Credit(Base):
    __tablename__ = 'credit'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('account.id'))
    amount: Mapped[float] = mapped_column(Float)
    term_months: Mapped[int] = mapped_column(Integer)
    balance: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime | None] = mapped_column(DateTime)

    def __repr__(self):
        return (f'<Credit(id={self.id}, '
                f'account_id={self.account_id}, '
                f'amount={self.amount}, '
                f'term_months={self.term_months}, '
                f'balance={self.balance}, '
                f'created_at={self.created_at})>')