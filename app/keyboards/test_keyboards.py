from aiogram import types

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

end_test_btn = InlineKeyboardBuilder()
end_test_btn.row(
    types.InlineKeyboardButton(
        text="Да",
        callback_data=f"liked_1"
    )
)
end_test_btn.row(
    types.InlineKeyboardButton(
        text="Нет",
        callback_data=f"liked_0"
    )
)
end_test_btn = end_test_btn.as_markup()


def get_test_btn(number_test: int) -> InlineKeyboardMarkup:
    btn = InlineKeyboardBuilder()
    btn.row(
        types.InlineKeyboardButton(
            text="1",
            callback_data=f"test_{number_test}_1"
        )
    )
    btn.row(
        types.InlineKeyboardButton(
            text="2",
            callback_data=f"test_{number_test}_2"
        )
    )
    btn.row(
        types.InlineKeyboardButton(
            text="3",
            callback_data=f"test_{number_test}_3"
        )
    )
    btn.row(
        types.InlineKeyboardButton(
            text="4",
            callback_data=f"test_{number_test}_4"
        )
    )
    btn = btn.as_markup()
    return btn
