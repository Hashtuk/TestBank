from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from Module_5.src.main.api.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime)

    def __repr__(self):
        return f'<User(id={self.id}, username={self.username}, role={self.role}, deleted_at={self.deleted_at})>'