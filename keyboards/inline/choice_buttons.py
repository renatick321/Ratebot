from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import buy_callback


def payment_btns(url, id, days):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('💰 Оплатить', url=url)
    btn2 = InlineKeyboardButton('✅ Проверить оплату', callback_data=f"pay|{id}|{days}")
    keyboard.row(btn1)
    keyboard.row(btn2)
    return keyboard

def free_channel_btn(url):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('📢 Перейти на канал', url=url)
    keyboard.row(btn1)
    return keyboard