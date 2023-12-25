from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


_IKM = InlineKeyboardMarkup
_IKB = InlineKeyboardButton

to_main = _IKM(
    inline_keyboard=[
        [_IKB(text="<< Вернуться в главное меню", callback_data="to_main")],
    ]
)

menu = _IKM(
    inline_keyboard=[
        [_IKB(text="Задания", callback_data="tasks")],
        [_IKB(text="Мой уровень", callback_data="my_lvl")],
        [_IKB(text="Контакты", callback_data="contacts")],
    ]
)

admin_menu = _IKM(
    inline_keyboard=[
        [_IKB(text="Удалить пользователя", callback_data="stop_bot")],
    ]
)

tasks = _IKM(
    inline_keyboard=[
        [_IKB(text="Подписаться на ВК", callback_data="subs_vk")],
        [_IKB(text="Подписаться на Instagram", callback_data="subs_inst")],
        [_IKB(text="Оставить отзыв в 2GIS картах", callback_data="feedback_2gis")],
        [_IKB(text="Оставить отзыв в Яндекс картах", callback_data="feedback_yandex")],
        [_IKB(text="<< Вернуться в главное меню", callback_data="to_main")],
    ]
)

task_admin_menu_vk = _IKM(
    inline_keyboard=[
        [
            _IKB(text="Принять", callback_data="accept_vk"),
            _IKB(text="Отклонить", callback_data="overrule_vk"),
        ],
    ]
)

task_admin_menu_inst = _IKM(
    inline_keyboard=[
        [
            _IKB(text="Принять", callback_data="accept_inst"),
            _IKB(text="Отклонить", callback_data="overrule_inst"),
        ],
    ]
)

task_admin_menu_2gis = _IKM(
    inline_keyboard=[
        [
            _IKB(text="Принять", callback_data="accept_2gis"),
            _IKB(text="Отклонить", callback_data="overrule_2gis"),
        ],
    ]
)

task_admin_menu_yandex = _IKM(
    inline_keyboard=[
        [
            _IKB(text="Принять", callback_data="accept_yandex"),
            _IKB(text="Отклонить", callback_data="overrule_yandex"),
        ],
    ]
)
