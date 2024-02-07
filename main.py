import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from root import TOKEN
from buttons import button, button_boy, button_girl
from inline_button import inline_btn
from images import *

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
    async def cmd_boy(message: types.Message):
        await message.answer("Bolalar kiyimlar ro'yhati", reply_markup=button_boy)

        @dp.message(F.text == "Bosh kiyim 🧢")
        async def cmd_bosh_kiyim(message: types.Message):
            for i in bosh_kiyim_boy:
                await message.answer_photo(photo=i, caption="Bosh kiyim 🧢", reply_markup=inline_btn)

        @dp.message(F.text == "Ustki kiyim 👕")
        async def cmd_ustki_kiyim(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg", caption="Ustki kiyim 👕",
                                       reply_markup=inline_btn)

        @dp.message(F.text == "Pastki kiyim 👖")
        async def cmd_pastki_kiyim(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/jjTdmbnL/kurtka.jpg", caption="Pastki kiyim 👖",
                                       reply_markup=inline_btn)

        @dp.message(F.text == "Oyoq kiyim 🥾")
        async def cmd_oyoq_kiyim(message: types.Message):
            for i in Oyoq_kiyimlar_boy:
                await message.answer_photo(photo=i, caption="Oyoq kiyim 🥾", reply_markup=inline_btn)

        @dp.message(F.text == "🔙 Orqaga qaytish")
        async def cmd_orqaga_boy(message: types.Message):
            await message.answer("Orqaga qaytildi", reply_markup=button)
            await message.delete()

    @dp.message(F.text == "Qiz 🙍‍♀️")
    async def cmd_girl(message: types.Message):
        await message.answer("Qizlar kiyimlar ro'yhati", reply_markup=button_girl)

        @dp.message(F.text == "Bosh kiyim 👒")
        async def cmd_bosh_kiy_girl(message: types.Message):
            for i in bosh_kiyim_girl:
                await message.answer_photo(photo=i, caption="Bosh kiyim 👒", reply_markup=inline_btn)

        @dp.message(F.text == "Ustki kiyim 👗")
        async def cmd_ustki_kiy_girl(message: types.Message):
            await message.answer_photo(photo="https://i.postimg.cc/SNn0h5kG/photo-94-2024-02-06-16-33-03.jpg",
                                       caption="Ustki Kiyim 👗", reply_markup=inline_btn)
            await message.answer_photo(photo="https://i.postimg.cc/3Rt6Mjq6/photo-89-2024-02-06-16-33-03.jpg",
                                       caption="Ustki Kiyim 👗", reply_markup=inline_btn)
            await message.answer_photo(photo="https://i.postimg.cc/BbdmsmBh/photo-57-2024-02-06-16-33-03.jpg",
                                       caption="Ustki Kiyim 👗", reply_markup=inline_btn)
            await message.answer_photo(photo="https://i.postimg.cc/fyhmyFJF/qiz.jpg",
                                       caption="Ustki Kiyim 👗", reply_markup=inline_btn)
            await message.answer_photo(photo="https://i.postimg.cc/TwcxKW4q/photo-96-2024-02-06-16-33-03.jpg",
                                       caption="Ustki Kiyim 👗", reply_markup=inline_btn)

        # @dp.message(F.text == "Pastki kiyim 👖")
        # async def cmd_pastki_kiy_girl(message: types.Message):
        #
        # @dp.message(F.text == "Oyoq kiyim 👠")
        # async def cmd_oyoq_kiy_girl(message: types.Message):

        @dp.message(F.text == "🔙 Orqaga qaytish")
        async def cmd_orqaga_girl(message: types.Message):
            await message.answer("Orqaga qaytildi", reply_markup=button)
            await message.delete()


@dp.callback_query(F.data == "alert")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(
        text="Batafsil ma'lumot olish uchun bosing:\nSotib Olish 🛒 ni bosing va Adminga murojaat qiling ✅",
        show_alert=True
    )


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
