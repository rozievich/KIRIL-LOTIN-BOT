from aiogram.fsm.state import State, StatesGroup


# Reklama uchun javobgar state
class AdsState(StatesGroup):
    ads = State()
