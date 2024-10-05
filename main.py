from datetime import timedelta

from services.get_messages_from_file import get_messages_from_file_
from services.whatsapp_summarizer import message_summarizer


def main():

    file_path = input("Enter the file path (MUST BE TXT): ")

    messages = get_messages_from_file_(file_path)

    last_2_days_messages = [
        message for message in messages if message.timestamp.date() > messages[-1].timestamp.date() - timedelta(days=2)
    ]

    summary = message_summarizer(last_2_days_messages)

    print(summary)


if __name__ == "__main__":
    main()
