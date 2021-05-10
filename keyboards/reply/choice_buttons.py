from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def remove_keyboard():
	keyboard = ReplyKeyboardRemove()
	return keyboard


def menu():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.row(KeyboardButton('💰 Тарифы'), KeyboardButton('📢 Бесплатный канал'))
	return keyboard


def rate_btns():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.row(KeyboardButton('👤 10$|30 дней'), KeyboardButton('🧑‍💻 27$|90 дней'), KeyboardButton('🧠 48$|180 дней'))
	keyboard.row(KeyboardButton('🕒 Пробный период'))	
	keyboard.row(KeyboardButton('🔙 Назад'))
	return keyboard