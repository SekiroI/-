from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.methods.send_message import SendMessage


from keyboards import (
    menu,
    to_main,
    admin_menu,
    tasks,
)
from database import (
    add_user,
    delete_user,
    set_user_lvl,
    get_user_lvl,
    task_complete,
    is_task_complete,
)
from states import (
    General,
    Tasks,
    Level,
    ChangeUserLVL,
)
from texts import user_texts, admin_texts, _tasks
from config import ADMIN_ID
from last_user import LastUser


router = Router()

#########################################################################
#                                                                       #
#                                                                       #
#                            COMMAND HANDLERS                           #
#                                                                       #
#                                                                       #
#########################################################################


@router.message(Command("start"))
async def start_handler(msg: Message):
    if msg.chat.id == ADMIN_ID:
        await msg.answer(
            admin_texts["start"].format(msg.chat.username),
            reply_markup=admin_menu,
        )
    else:
        add_user("test", "Users", msg.chat.id, msg.chat.username)
        await msg.answer(
            user_texts["start"].format(msg.chat.username, 1),
            reply_markup=menu,
        )


#########################################################################
#                                                                       #
#                                                                       #
#                         HANDLERS WITH CALLBACK                        #
#                                                                       #
#                                                                       #
#########################################################################


@router.callback_query(F.data == "to_main")
async def to_main_handler(clback: CallbackQuery, state: FSMContext):
    await state.set_state(General.menu_state)
    await clback.message.delete()
    await clback.message.answer(user_texts["to_main"], reply_markup=menu)


@router.callback_query(F.data == "tasks")
async def tasks_handler(clback: CallbackQuery, state: FSMContext):
    await state.set_state(General.tasks_state)
    await clback.message.delete()
    await clback.message.answer(user_texts["tasks"], reply_markup=tasks)


###############################  TASKS  ################################


@router.callback_query(F.data == "subs_vk")
async def subs_vk_handler(clback: CallbackQuery, state: FSMContext):
    if is_task_complete("test", "Users", clback.from_user.id, "task_1"):
        await clback.message.delete()
        await clback.message.answer(
            user_texts["task_is_complete"], reply_markup=to_main
        )
    else:
        await state.set_state(Tasks.subs_vk)
        await clback.message.delete()
        await clback.message.answer(user_texts["subs_vk"], reply_markup=to_main)


@router.callback_query(F.data == "subs_inst")
async def subs_inst_handler(clback: CallbackQuery, state: FSMContext):
    if is_task_complete("test", "Users", clback.from_user.id, "task_2"):
        await clback.message.delete()
        await clback.message.answer(
            user_texts["task_is_complete"], reply_markup=to_main
        )
    else:
        await state.set_state(Tasks.subs_inst)
        await clback.message.delete()
        await clback.message.answer(user_texts["subs_inst"], reply_markup=to_main)


@router.callback_query(F.data == "feedback_2gis")
async def feedback_2gis_handler(clback: CallbackQuery, state: FSMContext):
    if is_task_complete("test", "Users", clback.from_user.id, "task_3"):
        await clback.message.delete()
        await clback.message.answer(
            user_texts["task_is_complete"], reply_markup=to_main
        )
    else:
        await state.set_state(Tasks.feedback_2gis)
        await clback.message.delete()
        await clback.message.answer(user_texts["feedback_2gis"], reply_markup=to_main)


@router.callback_query(F.data == "feedback_yandex")
async def feedback_yandex_handler(clback: CallbackQuery, state: FSMContext):
    if is_task_complete("test", "Users", clback.from_user.id, "task_4"):
        await clback.message.delete()
        await clback.message.answer(
            user_texts["task_is_complete"], reply_markup=to_main
        )
    else:
        await state.set_state(Tasks.feedback_yandex)
        await clback.message.delete()
        await clback.message.answer(user_texts["feedback_yandex"], reply_markup=to_main)


###############################  LEVEL  ################################


@router.callback_query(F.data == "my_lvl")
async def my_lv_handler(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Level.my_lvl)
    await clback.message.delete()
    await clback.message.answer(
        user_texts["my_lvl"].format(
            get_user_lvl("test", "Users", clback.message.chat.id)
        ),
        reply_markup=to_main,
    )


##############################  CONTACTS  ###############################


@router.callback_query(F.data == "contacts")
async def contacts_handler(clback: CallbackQuery, state: FSMContext):
    await state.set_state(Level.my_lvl)
    await clback.message.delete()
    await clback.message.answer(
        user_texts["contacts"],
        reply_markup=to_main,
    )


###############################  ADMIN  ################################


@router.callback_query(F.data == "accept_vk")
async def accept_vk_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.accept_vk)
    task_complete("test", "Users", LastUser.get_last_user_id(), "task_1")
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_accept"].format(_tasks["task_1"]),
    )

@router.callback_query(F.data == "overrule_vk")
async def overrule_vk_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.overrule_vk)
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_overrule"].format(_tasks["task_1"]),
    )



@router.callback_query(F.data == "accept_inst")
async def accept_inst_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.accept_inst)
    task_complete("test", "Users", LastUser.get_last_user_id(), "task_2")
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_accept"].format(_tasks["task_2"]),
    )

@router.callback_query(F.data == "overrule_inst")
async def overrule_inst_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.overrule_inst)
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_overrule"].format(_tasks["task_2"]),
    )



@router.callback_query(F.data == "accept_2gis")
async def accept_2gis_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.accept_2gis)
    task_complete("test", "Users", LastUser.get_last_user_id(), "task_3")
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_accept"].format(_tasks["task_3"]),
    )

@router.callback_query(F.data == "overrule_2gis")
async def overrule_2gis_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.overrule_2gis)
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_overrule"].format(_tasks["task_3"]),
    )



@router.callback_query(F.data == "accept_yandex")
async def accept_yandex_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.accept_yandex)
    task_complete("test", "Users", LastUser.get_last_user_id(), "task_4")
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_accept"].format(_tasks["task_4"]),
    )

@router.callback_query(F.data == "overrule_yandex")
async def overrule_yandex_task(clback: CallbackQuery, state: FSMContext):
    await state.set_state(ChangeUserLVL.overrule_yandex)
    await clback.message.delete()
    return SendMessage(
        chat_id=LastUser.get_last_user_id(),
        text=user_texts["task_overrule"].format(_tasks["task_4"]),
    )