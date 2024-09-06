from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from http import HTTPStatus
from sqlalchemy.exc import NoResultFound
from Demo.api.schema.items_schema import ItemModelCommand, ItemResponseSchema
from Demo.db.services.items_services import ItemService
from Demo.db.factory import item_service_factory
item_router = APIRouter()

@item_router.post(
    "/items/",
    response_model=ItemResponseSchema,
)
def create_item(
        command: ItemModelCommand,
        item_service: Annotated[ItemService, Depends(item_service_factory)]
):
    try:
        return item_service.create_item(command)
    except NoResultFound:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Item creation failed")

@item_router.get(
    "/items/{item_id}",
    response_model=ItemResponseSchema,
)
def read_item(
        item_id: int,
        item_service: Annotated[ItemService, Depends(item_service_factory)]
):
    try:
        return item_service.get_item(item_id)
    except NoResultFound:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="ItemModel not found")

@item_router.put(
    "/items/{item_id}",
    response_model=ItemResponseSchema
)
def update_item(
        item_id: int,
        command: ItemModelCommand,
        item_service: Annotated[ItemService, Depends(item_service_factory)]
):
    try:
        return item_service.update_item(item_id, command)
    except NoResultFound:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="ItemModel not found")


@item_router.patch(
    "/items/{item_id}",
    response_model=ItemResponseSchema
)
def partial_update_item(
        item_id: int,
        item_service: Annotated[ItemService, Depends(item_service_factory)],
        name: str = None,
        city: str = None
):
    try:
        return item_service.partial_update_item(item_id, name, city)
    except NoResultFound:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="ItemModel not found")


@item_router.delete(
    "/items/{item_id}",
    status_code=HTTPStatus.OK
)
def delete_item_endpoint(
        item_id: int,
        item_service: Annotated[ItemService, Depends(item_service_factory)]
):
    try:
        return item_service.delete_item(item_id)
    except NoResultFound:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="ItemModel not found")
