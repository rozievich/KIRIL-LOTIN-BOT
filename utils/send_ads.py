from aiogram import types


async def send_adversment(msg: types.Message, user_id):
        try:
            await msg.copy_to(user_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_markup=msg.reply_markup)
            return 0
        except:
            return 1
