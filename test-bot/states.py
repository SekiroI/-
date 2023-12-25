from aiogram.fsm.state import StatesGroup, State


class General(StatesGroup):
    menu_state = State()
    tasks_state = State()
    lvl_state = State()
    contacts_state = State()


class Tasks(StatesGroup):
    subs_vk = State()
    subs_inst = State()
    feedback_2gis = State()
    feedback_yandex = State()


class Level(StatesGroup):
    my_lvl = State()


class ChangeUserLVL(StatesGroup):
    accept_vk = State()
    overrule_vk = State()
    accept_inst = State()
    overrule_inst = State()
    accept_2gis = State()
    overrule_2gis = State()
    accept_yandex = State()
    overrule_yandex = State()
