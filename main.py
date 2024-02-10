import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from root import TOKEN
from buttons import button, buton

dp = Dispatcher()


# async def startup_answer(bot: Bot):
#     await bot.send_message(5611541842, "Bot ishga tushdi! ✅")
#
#
# async def shutdown__answer(bot: Bot):
#     await bot.send_message(5611541842, "Bot ishga to'xtadi!❗️")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}", parse_mode=ParseMode.HTML, reply_markup=button)

    @dp.message(F.text == "O'g'il 🙍‍♂️")
    async def cmdd(message: types.Message):
        await message.answer("Kiyimlar ro'yhati", reply_markup=buton)

        @dp.message(F.text == "Bosh kiyim 🧢")
        async def cmdd(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg")

        @dp.message(F.text == "Ustki kiyim 👕")
        async def cmdd(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg")

        @dp.message(F.text == "Pastki kiyim 👖")
        async def cmdd(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg")

        @dp.message(F.text == "Oyoq kiyim 🥾")
        async def cmdd(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg")

        @dp.message(F.text == "Orqaga qaytish")
        async def cmd_orqaga(message: types.Message):
            await message.answer("Orqaga qaytildi", reply_markup=button)


async def main():
    # dp.startup.register(startup_answer)
    # dp.message.register(cmd_start)
    # dp.shutdown.register(shutdown__answer)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="start", description="Bot ishga tushirish"),
        BotCommand(command="help", description="Yordam")
    ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
