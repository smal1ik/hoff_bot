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


def get_test_btn(number_test: int, count_btn: int = 4) -> InlineKeyboardMarkup:
    btn = InlineKeyboardBuilder()
    row = []

    for i in range(1, count_btn + 1):
        row.append(
            types.InlineKeyboardButton(
                text=f"{i}",
                callback_data=f"test_{number_test}_{i}"
            )
        )
        if len(row) == 4:
            btn.row(*row)
            row = []

    return btn.as_markup()

