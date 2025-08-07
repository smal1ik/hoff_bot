from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


start_btn = InlineKeyboardBuilder()
start_btn.row(
    types.InlineKeyboardButton(
        text="Старт",
        callback_data="start")
)
start_btn = start_btn.as_markup()


accept_terms_btn = InlineKeyboardBuilder()
accept_terms_btn.row(
    types.InlineKeyboardButton(
        text="Соглашаюсь, вперёд к тесту",
        callback_data="accept_terms")
)
accept_terms_btn = accept_terms_btn.as_markup()

