from aiogram import types, Dispatcher
from bot_instance import bot

async def secret_word(message: types.Message):
    await message.reply("Yes, my master")

async def echo_and_ban(message: types.Message):
    ban_words = ['java', 'bitch', 'slut', 'python is bad']
    for i in ban_words:         # эти 4 строчки кода помогают удалить плохое слово и все предложение то что напечатали
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Bot Admin deleted bad words")
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)
    # elif message.text.lower() in ban_words:
    #     await bot.send_message(message.chat.id, "Bot-Admin deleted bad words")
    #     await message.delete()

    # else:   эти 2 строчки кода эхо бота
    #     await message.answer(message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
    dp.register_message_handler(echo_and_ban, content_types=['text'])