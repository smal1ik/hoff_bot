from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database.requests import get_user


class IsModerator(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user = await get_user(message.from_user.id)
        return user.is_moderator


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user = await get_user(message.from_user.id)
        return user.is_admin
