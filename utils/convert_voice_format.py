from pydub import AudioSegment
from io import BytesIO

# In order to voice message be usable for openAI API , it should be converted to certain file format .


async def convert_voice_format(voice_file, voice_format):
    """

    :param voice_file: voice file from user
    :param voice_format: format of voice
    :return: Byte object of convert voice
    """

    with open(voice_file, mode='rb') as voice_data:

        audio = AudioSegment.from_file(file=voice_data, format=voice_format)
        # from raw -> need to give byte object
        wav_file = BytesIO()
        # for Whisper api need to add name tag -> otherwise with just returning BytesIo will not work .
        wav_file.name = voice_file
        audio.export(wav_file, format='wav')

        return wav_file
