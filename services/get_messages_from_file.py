from datetime import datetime

from models.models import WhatsappMessage


def get_messages_from_file_(file_path: str) -> list[WhatsappMessage]:

    with open(file_path, "r") as f:
        lines = f.readlines()
        messages: list[WhatsappMessage] = []
        for line in lines:
            if line.startswith("["):
                start_index = line.index("[")
                end_index = line.index("]")
                if start_index + end_index < 18:
                    continue
                sender_end_index = line.index(":", end_index)
                timestamp = datetime.strptime(line[start_index + 1 : end_index], "%m/%d/%y, %I:%M:%S %p")
                sender = line[end_index + 1 : sender_end_index]
                message = line[sender_end_index + 1 :]
                messages.append(WhatsappMessage(message=message.strip(), sender=sender, timestamp=timestamp))
            else:
                messages[-1].message += line
    return messages
