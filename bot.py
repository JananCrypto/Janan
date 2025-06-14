 import logging
from telegram.ext import Updater, CommandHandler
import requests

# توکن ربات خود را اینجا وارد کنید
TOKEN = 8067181419:AAE-ofww9HWOi1oxDEm41FL42ulemFASbec

# تابع شروع
def start(update, context):
    update.message.reply_text("سلام! به ربات جانان خوش آمدید 🌟")

# تابع قیمت بیت‌کوین
def bitcoin(update, context):
    url = "https://api.coindesk.com/v1/bpi/currentprice/USDT.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    update.message.reply_text(f"قیمت فعلی بیت‌کوین: {price} دلار 💰")

# تابع اصلی
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("bitcoin", bitcoin))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
