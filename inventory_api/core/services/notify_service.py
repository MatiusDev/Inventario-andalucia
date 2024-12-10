from typing import Annotated
from fastapi import Depends
from sqlmodel import select

from config.db_adapter import DBSession

from models.entities.notify import Notify


class NotifyService:
    def __init__(self, db: DBSession) -> None:
        self.db = db
    
    
    def notifyChange(self, id_product:int, message:str):
        notify_db = Notify(
            id_product =  id_product,
            message = message
        )
        self.db.add(notify_db)
        self.db.commit()
    
    def list_notifications(self):
        notifications = self.db.exec(select(Notify)).all()


        return notifications

    
NotifyDependency = Annotated[NotifyService, Depends(NotifyService)]