from loader import dp, bot
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, Message, CallbackQuery
from keyboards.inline.choice_buttons import *
from keyboards.reply.choice_buttons import *
from data import db
from config import ADMIN, client, CHANNEL_ID
from aiogram.utils.exceptions import ChatNotFound
import xlrd, xlwt
from aiogram.dispatcher import FSMContext
from data.api import payment
import asyncio


@dp.message_handler(Command('start'))  # Начало начал
async def start_command(message):
    await message.answer("Привет! Тут текст приветствия!", reply_markup=menu())



@dp.message_handler()
async def text_msg(message):
    s = message.text
    if s == '💰 Тарифы':
        await message.answer("Оплатитите доступ", reply_markup=rate_btns())
    elif s == '👤 10$|30 дней':
        charge = payment.charge_create(10)
        url = charge['hosted_url']
        id = charge['id']
        await message.answer("Оплатите доступ", reply_markup=payment_btns(url, id, 30))
    elif s == '🧑‍💻 27$|90 дней':
        charge = payment.charge_create(27)
        url = charge['hosted_url']
        id = charge['id']
        await message.answer("Оплатите доступ", reply_markup=payment_btns(url, id, 90))
    elif s == '🧠 48$|180 дней':
        charge = payment.charge_create(48)
        url = charge['hosted_url']
        id = charge['id']
        await message.answer("Оплатите доступ", reply_markup=payment_btns(url, id, 180))
    elif s == '🕒 Пробный период':
        if db.get_free(message.chat.id):
            task = dp.loop.create_task(client.create_chat_invite_link(CHANNEL_ID, member_limit=1))
            await asyncio.gather(task)
            link = task.result()['invite_link']
            await message.answer(f"Ссылка приглашение для вашего аккаунта: {link}")
        else:
            await message.answer("Вы уже получали бесплатное приглашение в приватный канал")
    elif s == '📢 Бесплатный канал':
        await message.answer("📢 Бесплатный канал")
    elif s == '🔙 Назад':
        await message.answer("Вы в главном меню", reply_markup=menu())
    else:
        await message.answer("Вы в главном меню", reply_markup=menu())



@dp.callback_query_handler(lambda call: "pay" in call.data)
async def dislike(call: CallbackQuery):
    charge_id, days = map(str, call.data[4:].split("|"))
    charge = payment.get_charge(charge_id)
    print(charge)
    if charge['timeline'][-1]['status'] == 'COMPLETED':
        db.get_free(call.message.chat.id)
        db.user_save(call.message.chat.id, int(days))
        link = ['invite_link']
        task = dp.loop.create_task(client.create_chat_invite_link(CHANNEL_ID, member_limit=1))
        await asyncio.gather(task)
        link = task.result()['invite_link']
        await call.message.answer(f"Ссылка приглашение для вашего аккаунта: {link}")
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        await call.message.answer("Оплата не прошла. Попробуйте снова")