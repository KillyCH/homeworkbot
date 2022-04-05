from aiogram import Bot, executor
from bot_instance import dp
from handers import client, callback, extra, fsmadmin
from database import bot_db

async def on_startup(_):
    bot_db.sql_create()


fsmadmin.register_handler_fsadmin(dp)
client.register_handlers_client(dp)
callback.register_handler_callback(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
