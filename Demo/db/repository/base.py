from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from Demo.db.models.items_models import Base

def create_entity(session: Session, entity: Base):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    if not entity:
        raise NoResultFound
    return entity

def update_entity(session: Session, entity: Base):
    session.commit()
    session.refresh(entity)
    if not entity:
        raise NoResultFound
    return entity

def partial_update_entity(session: Session, entity: Base, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            setattr(entity, key, value)
    session.commit()
    session.refresh(entity)
    if not entity:
        raise NoResultFound
    return entity

def delete_entity(session: Session, entity: Base):
    session.delete(entity)
    session.commit()
    if not entity:
        raise NoResultFound
    return True

def get_entity_by_id(session: Session, entity: Base, id: int):
    entity = session.query(entity).filter(entity.id == id).first()
    if not entity:
        raise NoResultFound
    return entity
