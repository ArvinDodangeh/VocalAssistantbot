from services.OpenAI_Instance import client
import logging


async def voice_to_text(raw_audio_file):

    try:

        # Send raw bytes to OpenAI Whisper API
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=raw_audio_file
        )
        transcript_text = transcription.text
        return transcript_text

    except Exception as e:
        logging.info(f'Error happened during transformation {e}')
