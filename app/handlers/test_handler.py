import asyncio
from pathlib import Path

from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import app.utils.copy as cp
import app.keyboards.test_keyboards as kb

from decouple import config as env_config

from app.database.requests import add_answer_test, edit_liked_test

GLOBAL_PATH = env_config("GLOBAL_PATH")

test_handler = Router()


@test_handler.callback_query(F.data == 'accept_terms')
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_data({"answers": []})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + '/assets/images/1.png')),
        reply_markup=kb.get_test_btn(1)
    )



@test_handler.callback_query(F.data.contains("test_1"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(int(callback.data.split("_")[2]))
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/2.png")),
        reply_markup=kb.get_test_btn(2)
    )


@test_handler.callback_query(F.data.contains("test_2"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/3.png")),
        reply_markup=kb.get_test_btn(3)
    )


@test_handler.callback_query(F.data.contains("test_3"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/4.png")),
        reply_markup=kb.get_test_btn(4)
    )


@test_handler.callback_query(F.data.contains("test_4"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/5.png")),
        reply_markup=kb.get_test_btn(5)
    )


@test_handler.callback_query(F.data.contains("test_5"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/6.png")),
        reply_markup=kb.get_test_btn(6)
    )


@test_handler.callback_query(F.data.contains("test_6"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/7.png")),
        reply_markup=kb.get_test_btn(7)
    )


@test_handler.callback_query(F.data.contains("test_7"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/8.png")),
        reply_markup=kb.get_test_btn(8, 8)
    )


@test_handler.callback_query(F.data.contains("test_8"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])
    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.update_data({"answers": data})
    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + "/assets/images/9.png")),
        reply_markup=kb.get_test_btn(9)
    )


@test_handler.callback_query(F.data.contains("test_9"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    number_answer = int(callback.data.split("_")[2])

    data = (await state.get_data())["answers"]
    data.append(number_answer)
    await state.clear()

    await add_answer_test(callback.from_user.id, data)

    max_count_answer, text_answer = cp.get_answer_test_msg(data)

    await callback.message.answer_photo(
        photo=FSInputFile(Path(GLOBAL_PATH + f"/assets/images/result_{max_count_answer}.png")),
        caption=text_answer,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await asyncio.sleep(1)
    await callback.message.answer(cp.end_test_msg, reply_markup=kb.end_test_btn, parse_mode="HTML", disable_web_page_preview=True)


@test_handler.callback_query(F.data.contains("liked"))
async def answer_message(callback: types.CallbackQuery, state: FSMContext):
    is_liked = bool(int(callback.data.split("_")[1]))
    await edit_liked_test(callback.from_user.id, is_liked)
