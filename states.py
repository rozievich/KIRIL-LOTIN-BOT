from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    comments = State()


class AdverState(StatesGroup):
    adver = State()


class AddState(StatesGroup):
    index = State()


class DelState(StatesGroup):
    deladmin = State()
