import io
from aiogram import Bot

from data.translation import to_cyrillic
from utils.db_data import session, Channel


async def is_subscribed_to_channels(user_id: int, bot: Bot):
    channels = session.query(Channel).all()
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel.channel_id, user_id=user_id)
        if chat_member.status == 'left':
            return False
    return True


# Faylni transliteratsiya qiluvchi funksiyasi
def transliterate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Har bir qatorni transliteratsiya qilib, yangi faylga yozamiz
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            transliterated_line = to_cyrillic(line)
            f.write(transliterated_line)


# Faylni transliteratsiya qiluvchi funksiyasi
async def transliterate_and_send(input_file_content: str):
    # Har bir qatorni transliteratsiya qilib, yangi faylga yozamiz
    output_content = io.BytesIO()

    # Transliteratsiya qilish
    for line in input_file_content.splitlines(keepends=True):
        transliterated_line = to_cyrillic(line)
        output_content.write(transliterated_line.encode('utf-8'))

    output_content.seek(0)  # Faylni boshidan o'qish

    return output_content
