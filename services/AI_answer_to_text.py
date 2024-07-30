from services.OpenAI_Instance import client


def openai_response(transcript_text: str) -> str:
    """

    :param transcript_text: text which has been gotten by client voice note

    :return: OpenAI's language model to that text

    """
    assistant = client.beta.assistants.create(
        name='Personal Assistant',
        instructions='Answer question in short and structural format',
        model='gpt-4o'
    )

    # Creating threads
    thread = client.beta.threads.create()
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions=transcript_text
    )

    answer_text = ''
    if run.status == 'completed':
        answer = client.beta.threads.messages.list(thread_id=thread.id)
        # Extract the latest message's text content
        if answer and answer.data:
            latest_message = answer.data[-1]  # Assuming the latest message is the last one
            if latest_message.content and latest_message.content[0].type == 'text':
                answer_text = latest_message.content[0].text.value
    return answer_text
