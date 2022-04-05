from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from bot_instance import Dispatcher, bot
from database import bot_db
from keyboard import keyboard

async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                            f"Hello my master: {message.from_user.full_name}",
                            reply_markup=keyboard.keyboard_stat)

async def quiz_1(message: types.Message):
    question = "By whom invented Python"
    answer = ["Harry Potter", "Voldemort", "Gvido Van ROssum", "Linus Torvalds"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        explanation="This is easy, not gonna tell you",
                        explanation_parse_mode=ParseMode.MARKDOWN_V2)

async def problem_1(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След задача",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Output:"
    answer = ['0.0', '4', '0', '8', '8.0', "Error"]
    photo = open("media/photo5276270132777302129.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question,
        options=answer,
        is_anonymous=False,
        correct_option_id=0,
        type='quiz',
        reply_markup=markup
    )

async def show_all_anime_command(message: types.Message):
    await bot_db.sql_command_select(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(problem_1, commands=['problem'])
    dp.register_message_handler(show_all_anime_command, commands=['anime'])