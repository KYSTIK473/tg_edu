import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6639863467:AAHVLpkZ42zNmWi9mi1MCuotlK42NlJ5ZPU")
# Диспетчер
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
