from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from Demo.db.services.items_services import ItemService
from Demo.db.DataBasa.postgres import get_db

def item_service_factory(
        session: Annotated[Session, Depends(get_db)]):
    return ItemService(session)
