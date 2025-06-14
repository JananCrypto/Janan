import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode

# ربات توکن را از متغیر محیطی می‌گیرد
TOKEN = os.getenv("BOT_TOKEN")

# پیکربندی لاگ
logging.basicConfig(level=logging.INFO)

# ایجاد نمونه‌های بات و دیسپچر
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# پاسخ ساده به فرمان /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! 👋\nمن ربات جانان هستم. آماده‌ام تا اخبار و قیمت‌های رمزارز را برایت ارسال کنم.")

# اجرای ربات
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
