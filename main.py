import logging
import asyncio
import sys
from handlers.message_handler import receive_voice_router
from handlers.command_handler import Start_Command_router
from aiogram import Dispatcher
from bot.bot_instance import bot


async def register_handler(dp: Dispatcher) -> None:
    """

    :param dp: Dispatcher from aiogram
    :return: This function set register router for handler
    """
    dp.include_router(Start_Command_router)
    dp.include_router(receive_voice_router)


async def main() -> None:
    """

    :return: The main function which run our telegram bot
    """
    dp = Dispatcher()
    await register_handler(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
