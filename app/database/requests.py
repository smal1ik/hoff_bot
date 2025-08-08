from datetime import datetime
from typing import List

from app.database.models import User, async_session
from sqlalchemy import select, BigInteger, update, delete, func, case


async def add_user(tg_id: BigInteger, first_name: str, username: str, full_name: str):
    """
    Функция добавляет пользователя в БД
    """
    async with async_session() as session:
        session.add(User(
            tg_id=tg_id,
            first_name=first_name,
            username=username,
            full_name=full_name))
        await session.commit()


async def get_user(tg_id: BigInteger) -> User:
    """
    Получаем пользователя по tg_id
    """
    async with async_session() as session:
        result = await session.scalar(select(User).where(User.tg_id == tg_id))
        return result


async def add_answer_test(tg_id: BigInteger, answer_test: List[int]):
    """
    Добавляем ответы на тест
    """
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(answer_test=answer_test))
        await session.commit()


async def edit_liked_test(tg_id: BigInteger, liked: bool):
    """
    Меняем нравится ли тест
    """
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(liked_test=liked))
        await session.commit()


async def get_all_users() -> List[User]:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.answer_test.isnot(None)))
        return result.scalars().all()

