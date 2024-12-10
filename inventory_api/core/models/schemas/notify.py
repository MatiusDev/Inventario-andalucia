from sqlmodel import SQLModel, Field

from models.entities.notify import Notify


class NotifyBase(SQLModel):
    message:str
    date_notification: str

class NotifyCreate(NotifyBase):
    pass

class NotifyRead(NotifyBase):
    id: int | None
    message:str
    date_notification: str
