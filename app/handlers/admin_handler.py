import json
import os

from aiogram import Router, types
from aiogram.filters.command import Command

from app.database.requests import get_all_users
from app.filters.admin_filter import IsAdmin

from datetime import datetime as dt
from decouple import config as env_config
from openpyxl import Workbook, load_workbook

admin_handler = Router()

@admin_handler.message(Command('excel'), IsAdmin())
async def excel(message: types.Message):
    headers = [
        "Номер участника",
        "1 вопрос", "2 вопрос", "3 вопрос", "4 вопрос", "5 вопрос",
        "6 вопрос", "7 вопрос", "8 вопрос", "9 вопрос",
        "Каких вариантов ответа больше",
        "Понравился тест"
    ]

    users = await get_all_users()

    # Создаём Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Users"
    ws.append(headers)

    # Заполняем
    for u in users:

        row = []
        row.append(u.tg_id)  # можно заменить на u.tg_id, если нужно

        for answer in u.answer_test:
            row.append(answer)

        count_answers = {}
        for elem in u.answer_test:
            count_answers[elem] = count_answers.get(elem, 0) + 1

        # Каких вариантов ответа больше
        max_count = max(count_answers, key=count_answers.get)
        row.append(max_count)

        # Итог Вопрос: понравился тест
        row.append(u.liked_test)

        ws.append(row)

    # Сохраняем
    filename = f"users_{dt.now().strftime('%Y%m%d')}.xlsx"
    filepath = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)
    wb.save(filepath)

    # Отправляем в Telegram
    await message.answer_document(types.FSInputFile(filepath))

    # Удаляем временный файл
    os.remove(filepath)