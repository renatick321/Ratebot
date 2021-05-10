from loader import bot
from config import ADMIN, CHANNEL_ID, client, format_
import asyncio
from utils import get_members_id, kick_chat_member
import data.db as db
import datetime


async def on_shutdown(dp):
    await bot.send_message(chat_id=ADMIN, text="Бот окончил свою работу")
    await bot.close()

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN, text="Бот запущен")

async def kick_users():
    while True:
        print(1)
        await asyncio.sleep(60)
        users = db.get_users()
        now = datetime.datetime.now()
        conscripts = list(filter(lambda x: now > datetime.datetime.strptime(list(x.keys())[0], format_), users))
        conscripts = list(map(lambda x: list(x.values())[0], conscripts))
        for i in conscripts:
            db.user_del(i)
            dp.loop.create_task(kick_chat_member(i))


async def kick_slaves():
    while True:
        print(2)
        await asyncio.sleep(18000) # раз в 5 часов
        users = list(map(lambda x: list(x.values())[0], db.get_users()))
        task = dp.loop.create_task(get_members_id())
        await asyncio.gather(task)
        slaves = task.result()
        now = datetime.datetime.now()
        conscripts = list(filter(lambda x: x not in users, slaves))
        for i in conscripts:
            dp.loop.create_task(kick_chat_member(i))


async def fuck():
	task = dp.loop.create_task(get_members_id())
	await asyncio.gather(task)
	print(task.result())



if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    client.start()
    dp.loop.create_task(kick_users())
    dp.loop.create_task(kick_slaves())
    #dp.loop.create_task(fuck())
    executor.start_polling(dp, on_startup=send_to_admin, on_shutdown=on_shutdown)