from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.methods.send_message import SendMessage

from states import Tasks
from texts import user_texts, admin_texts
from keyboards import to_main, task_admin_menu_vk, task_admin_menu_inst, task_admin_menu_2gis, task_admin_menu_yandex
from config import ADMIN_ID
from last_user import LastUser

admin_router = Router()


@admin_router.message(Tasks.subs_vk)
async def check_user_task_vk(msg: Message):
    await msg.answer(user_texts["wait_on_getting_data"], reply_markup=to_main)
    LastUser(msg.chat.id)
    return SendMessage(
        chat_id=ADMIN_ID,
        text=admin_texts["on_check"].format(msg.chat.id, msg.text),
        reply_markup=task_admin_menu_vk,
    )

@admin_router.message(Tasks.subs_inst)
async def check_user_task_inst(msg: Message):
    await msg.answer(user_texts["wait_on_getting_data"], reply_markup=to_main)
    LastUser(msg.chat.id)
    return SendMessage(
        chat_id=ADMIN_ID,
        text=admin_texts["on_check"].format(msg.chat.id, msg.text),
        reply_markup=task_admin_menu_inst,
    )

@admin_router.message(Tasks.feedback_2gis)
async def check_user_task_2gis(msg: Message):
    await msg.answer(user_texts["wait_on_getting_data"], reply_markup=to_main)
    LastUser(msg.chat.id)
    return SendMessage(
        chat_id=ADMIN_ID,
        text=admin_texts["on_check"].format(msg.chat.id, msg.text),
        reply_markup=task_admin_menu_2gis,
    )

@admin_router.message(Tasks.feedback_yandex)
async def check_user_task_yandex(msg: Message):
    await msg.answer(user_texts["wait_on_getting_data"], reply_markup=to_main)
    LastUser(msg.chat.id)
    return SendMessage(
        chat_id=ADMIN_ID,
        text=admin_texts["on_check"].format(msg.chat.id, msg.text),
        reply_markup=task_admin_menu_yandex,
    )
