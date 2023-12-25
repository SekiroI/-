import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import API_TOKEN
from handlers import router
from admin import admin_router


async def main():
    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router, admin_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="./logs/logging.log",
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    asyncio.run(main())
