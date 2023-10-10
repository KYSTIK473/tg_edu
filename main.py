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


# Хэндлер на команду /start
@dp.message_handler(commands=['start'], commands_prefix="/")
async def cmd_start(message: types.Message):
    await message.answer(message.from_user.username)


@dp.message_handler(lambda message: message.text == 'мой id')
async def cmd_id_user(message: types.Message):
    await message.answer(message.from_user.id)


@dp.message_handler(commands=['echo'], commands_prefix="/")
async def cmd_stop(message: types.Message):
    print(message.text)
    await message.answer(message.text)


@dp.message_handler(commands=['button'], commands_prefix="/")
async def cmd_stop(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton('Первая кнопка!', callback_data='button1')]
    keyboard.add(*buttons)
    await message.answer("Ура, кнопка", reply_markup=keyboard)


@dp.callback_query_handler()
async def callbacks_num(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, call.data)


@dp.message_handler(commands=['info'], commands_prefix="/")
async def cmd_info(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [KeyboardButton('/start'), KeyboardButton('/button'), KeyboardButton('/info'), KeyboardButton('мой id'),
               KeyboardButton('Просто так'), KeyboardButton('/del_but')]
    keyboard.add(*buttons)
    await message.answer("Список команд ниже", reply_markup=keyboard)


@dp.message_handler(commands=['del_but'], commands_prefix="/")
async def cmd_stop(message: types.Message):
    await message.answer("Убрали клавиатуру", reply_markup=ReplyKeyboardRemove())


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
