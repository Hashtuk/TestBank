from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from Module_5.src.main.api.db.base import Base


class Account(Base):
    __tablename__ = 'account'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    number: Mapped[str] = mapped_column(String, unique=True)
    balance: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return f'<Account(id={self.id}, user_id={self.user_id}, number={self.number}, balance={self.balance})>'