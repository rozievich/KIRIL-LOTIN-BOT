from aiogram import types


async def send_adversment(msg: types.Message, user_id):
        try:
            await msg.copy_to(user_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_markup=msg.reply_markup)
        except:
            return 1
        else:
            return 0   