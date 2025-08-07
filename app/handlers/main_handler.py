from aiogram import Router, types, Bot, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

import app.utils.copy as cp
import app.keyboards.main_keyboards as kb

from app.database.requests import add_user, get_user

main_handler = Router()


@main_handler.message(Command('start'))
async def cmd_message(message: types.Message, state: FSMContext, bot: Bot):
    print(await get_user(message.from_user.id))
    if not await get_user(message.from_user.id):
        await add_user(message.from_user.id,
                       message.from_user.first_name,
                       message.from_user.username,
                       message.from_user.full_name)
    else:
        # TODO: Логика для уже зарегистрированных пользователей
        pass

    await message.answer(cp.start_msg, parse_mode="HTML", reply_markup=kb.start_btn)


@main_handler.callback_query(F.data == 'start')
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(cp.terms_msg, parse_mode="HTML",
                                  reply_markup=kb.accept_terms_btn,
                                  disable_web_page_preview=True)
