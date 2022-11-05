from aiogram import Bot, Dispatcher, executor, types
from config import token, chat


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

keyWords = ["дом", "квартир", "купит", "куплю", "купим"]


@dp.message_handler(content_types=['text'])
async def send_message(message: types.Message):
    # await message.answer(message.text)

    if message.from_user.is_bot == False:
        for i in keyWords:
            if i in message.text.lower():
                # await message.answer(message.text)
                # await message.answer(message.from_user.is_bot)
                await message.reply('Вы ищите квартиру?')
                n = [message.from_user.username, message.from_user.first_name]
                await bot.send_message(chat_id=chat, text=n)

                return


if __name__ == '__main__':
    executor.start_polling(dp)
