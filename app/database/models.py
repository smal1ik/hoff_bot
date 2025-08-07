from typing import List
from datetime import datetime
from sqlalchemy import BigInteger, Boolean, JSON, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from decouple import config
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(config("POSTGRESQL"), echo=False)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    first_name: Mapped[str] = mapped_column()
    full_name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    datetime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    answer_test: Mapped[JSON] = mapped_column(JSON, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    liked_test: Mapped[bool] = mapped_column(Boolean, nullable=True)
