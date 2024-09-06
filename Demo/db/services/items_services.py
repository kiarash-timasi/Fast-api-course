from sqlalchemy.orm import Session
from Demo.db.models.items_models import ItemModel
from Demo.api.schema.items_schema import ItemModelCommand, ItemResponseSchema
from Demo.db.repository.base import create_entity, get_entity_by_id, update_entity, partial_update_entity, delete_entity

class ItemService:
    def __init__(self, session: Session):
        self.session = session

    def create_item(self, command: ItemModelCommand):
        item = ItemModel(id=command.id, name=command.name, city=command.city)
        return create_entity(self.session, item)

    def get_item(self, item_id: int):
        item = get_entity_by_id(self.session, ItemModel, id=item_id)
        return item

    def update_item(self, item_id: int, command: ItemModelCommand):
        item = get_entity_by_id(self.session, ItemModel, id=item_id)
        if item:
            item.name = command.name
            item.city = command.city
            return update_entity(self.session, item)
        return None

    def partial_update_item(self, item_id: int, name: str = None, city: str = None):
        item = get_entity_by_id(self.session, ItemModel, item_id, )
        if item:
            return partial_update_entity(self.session, item, name=name, city=city)
        return None

    def delete_item(self, item_id: int):
        item = get_entity_by_id(self.session, ItemModel, item_id)
        if item:
            return delete_entity(self.session, item)
        return False
