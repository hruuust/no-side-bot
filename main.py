import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputMediaPhoto
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("7876593735:AAG34rjMEY3UtShcbXv1W9VnbzcQNfgajtQ")
CHANNEL_ID = os.getenv("@NoSideNews")
ADMIN_ID = int(os.getenv("296214662"))

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Бот активен и готов публиковать новости.")

async def post_news(news_text, media_urls, source, lang='ru'):
    suffix = "…но скоро всё наладится." if lang == 'ru' else "...but things will get better soon."
    caption = f"{news_text}

Источник: {source}

{suffix}"
    if media_urls:
        media = [InputMediaPhoto(url) for url in media_urls]
        media[0].caption = caption
        media[0].parse_mode = "HTML"
        await bot.send_media_group(CHANNEL_ID, media)
    else:
        await bot.send_message(CHANNEL_ID, caption, parse_mode="HTML")
    await bot.send_message(ADMIN_ID, f"Опубликовано:
{news_text[:100]}...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
