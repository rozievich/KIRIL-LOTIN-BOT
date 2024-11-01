from aiogram.fsm.state import State, StatesGroup


# Reklama uchun javobgar statelar
class AdsState(StatesGroup):
    ads = State()


# Kanallar uchun javobgar statelar
class ChannelAddState(StatesGroup):
    url = State()
    channel_id = State()

class ChannelDeleteState(StatesGroup):
    channel_id = State()
