from aiogram.fsm.state import State, StatesGroup


# Reklama uchun javobgar statelar
class AdsState(StatesGroup):
    ads = State()


# Kanallar uchun javobgar statelar
class ChannelAddState(StatesGroup):
    url = State()
    user_id = State()

class ChannelDeleteState(StatesGroup):
    user_id = State()
