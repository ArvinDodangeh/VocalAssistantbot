from aiogram import html
import logging
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

Start_Command_router = Router()


@Start_Command_router.message(Command('start'))
async def command_start(message: Message) -> None:
    """

    This handler deal with /start command

    :param message: It's text which is message from the user

    :return: text to respond /start command

    """
    logging.info(f"/start command received from {message.from_user.full_name}")
    await message.answer(f'Hello , {html.bold(message.from_user.full_name)}😍')
