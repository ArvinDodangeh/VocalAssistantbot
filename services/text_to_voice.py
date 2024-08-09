from services.OpenAI_Instance import client


async def text_to_voice(text: str):
    """

    :param text:  Text from Open AI model

    :return: return Audio in Byte

    """

    # Make tts request :
    tts_response = client.audio.speech.create(
        model='tts-1',
        voice='alloy',
        input=text
    )
    audio = tts_response.response
    file_in_byte = b''.join([byte for byte in audio.iter_bytes()])

    return file_in_byte
