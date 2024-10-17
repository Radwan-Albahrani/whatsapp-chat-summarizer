import google.generativeai as genai

from config import GeminiApi
from models.models import WhatsappMessage


def message_summarizer(messages: list[WhatsappMessage]) -> str:
    """
    Summarizes the messages by sender

    """

    gemini_api = GeminiApi()
    genai.configure(api_key=gemini_api.key.get_secret_value())
    model = genai.GenerativeModel("gemini-1.5-flash")

    anonymized_messages, sender_to_anonymized_sender_mapping = _anonymize_all_senders(messages)

    messages_as_str = "\n".join([f"{an_message.sender}: {an_message.message}" for an_message in anonymized_messages])

    prompt = gemini_api.prompt.format(messages=messages_as_str)
    response = model.generate_content(prompt).text

    de_anonymized_response = response
    for sender, anonymized_sender in sender_to_anonymized_sender_mapping.items():
        de_anonymized_response = de_anonymized_response.replace(anonymized_sender, sender)

    return de_anonymized_response


def _anonymize_all_senders(messages: list[WhatsappMessage]) -> tuple[list[WhatsappMessage], dict[str, str]]:
    """
    Anonymizes all senders in the messages

    """

    set_of_senders = {message.sender for message in messages}
    sender_to_anonymized_sender_mapping = {sender: f"Sender {i}" for i, sender in enumerate(set_of_senders)}
    anonymized_messages = [
        message.model_copy(update={"sender": sender_to_anonymized_sender_mapping[message.sender]})
        for message in messages
    ]

    return anonymized_messages, sender_to_anonymized_sender_mapping
