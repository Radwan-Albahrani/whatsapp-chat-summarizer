from datetime import datetime

from pydantic import BaseModel


class WhatsappMessage(BaseModel):
    message: str
    sender: str
    timestamp: datetime
