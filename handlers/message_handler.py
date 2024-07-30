import logging
import tempfile
from services.voice_to_text import voice_to_text
from services.AI_answer_to_text import openai_response
from services.text_to_voice import text_to_voice
from bot.bot_instance import bot
from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from utils.convert_voice_format import convert_voice_format

receive_voice_router = Router()


@receive_voice_router.message()
async def receive_voice_message(message: Message) -> None:
    """

    :param message: Message is voice which we get from user

    :return: temp file which has save the voice note .

    """
    logging.info('Record your voice')
    try:
        voice = message.voice
        voice_format = voice.mime_type.split('/', -1)[-1]
        # getting feedback about voice format
        logging.info(f'voice format , type of it  {voice_format, type(voice_format)}')

        file_info = await bot.get_file(voice.file_id)
        file_path = file_info.file_path

        # Downloading voice file:
        voice_data = await bot.download_file(file_path=file_path)
        print(f"Downloaded data type: {type(voice_data)}")

        # voice_data is BytesIo, but it needs to be bytes in order to save in tempfile
        voice_byte = voice_data.read()

        print(f"Downloaded data byte : {type(voice_byte)}")

        with tempfile.NamedTemporaryFile(suffix=f'.{voice_format}', delete=False) as TempFile:
            logging.info(f'Created temp file {TempFile.name} , type of file {type(TempFile)}')

            TempFile.write(voice_byte)

        # format voice to wav :
        wav_voice_file = convert_voice_format(TempFile.name, voice_format)
        logging.info(f'Type of waw voice converted file {wav_voice_file}')

        TempFile.close()

        # Sending transcript text to bot
        transcript_text = voice_to_text(raw_audio_file=wav_voice_file)

        # Answer of Open Ai assistant to transcript text :
        assistant_answer = openai_response(transcript_text=transcript_text)

        # Sending Open AI message as voice to user :
        # Function text-to-voice return byte
        response_byte = text_to_voice(assistant_answer)
        # we need to convert file then send it as audio to user
        response_voice = BufferedInputFile(response_byte, filename='Audio_Response')
        await message.answer_voice(response_voice)

    except Exception as e:
        logging.info(f'Exceptions happened {e}')
