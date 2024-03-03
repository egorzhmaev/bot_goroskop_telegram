from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, Router, F
import asyncio
from get_text import get_text_horoscope
import datetime

router: Router = Router()

BOT_TOKEN = ''

ru = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
      7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

zd = {'aries': '\U00002648', 'taurus': '\U00002649', 'gemini': '\U00002650', 'cancer': '\U00002651', 'leo': '\U00002652', 'virgo': '\U00002653',
      'libra': '\U00002654', 'scorpio': '\U00002655', 'sagittarius': '\U00002656', 'capricorn': '\U00002657', 'aquarius': '\U00002658', 'pisces': '\U00002659'}
def get_zodiac_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Овен', callback_data='aries')
    keyboard_builder.button(text='Телец', callback_data='taurus')
    keyboard_builder.button(text='Близнецы', callback_data='gemini')
    keyboard_builder.button(text='Рак', callback_data='cancer')
    keyboard_builder.button(text='Лев', callback_data='leo')
    keyboard_builder.button(text='Дева', callback_data='virgo')
    keyboard_builder.button(text='Весы', callback_data='libra')
    keyboard_builder.button(text='Скорпион', callback_data='scorpio')
    keyboard_builder.button(text='Стрелец', callback_data='sagittarius')
    keyboard_builder.button(text='Козерог', callback_data='capricorn')
    keyboard_builder.button(text='Водолей', callback_data='aquarius')
    keyboard_builder.button(text='Рыбы', callback_data='pisces')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text='Привет. Выбери свой знак зодиака:', reply_markup=get_zodiac_keyboard())

@router.message(F.text)
async def answer(message: Message):
    await message.answer(text='Я не отвечаю на сообщения. И даже их удаляю. Поддерживаю порядок во вселенной \U0001F30C \n\nВыбери знак зодиака.', reply_markup=get_zodiac_keyboard())
    await message.delete()

@router.callback_query()
async def get_horoscope(call: CallbackQuery):
    await call.answer()
    zodiac = call.data
    text = await get_text_horoscope(zodiac=zodiac)
    month_now = ru.get(datetime.date.today().month)
    day_now = datetime.date.today().day
    await call.message.edit_text(text=f'Сегодня {day_now} {month_now} {zd.get(zodiac)} \n\n{text}\U0001F4AB\U0001FA90\U0001F30C')
    await call.message.answer(text='Посмотреть другой знак зодиака.', reply_markup=get_zodiac_keyboard())


async def start():
    bot: Bot = Bot(token=BOT_TOKEN)

    dp: Dispatcher = Dispatcher()

    dp.include_router(router=router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
