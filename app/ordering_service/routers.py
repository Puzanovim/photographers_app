from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import async_db_session
from app.ordering_service.models_api import OrderAPI
from app.ordering_service.schemas import OrderDB, OrderUpdate, OrderFullCreate, OrderFullDB, CommentCreate, \
    CommentUpdate, CommentDB
from app.ordering_service.service import get_user_orders, get_user_order, create_user_order, update_user_order, \
    create_order_comment, update_order_comment
from app.user_service.auth import get_current_user, is_performer_or_customer
from app.user_service.schemas import UserDB

router = APIRouter()
order_api = OrderAPI()


@router.get("/{user_id}/orders", response_model=List[OrderDB])
async def get_orders(
        user_id: UUID, db: AsyncSession = Depends(async_db_session), current_user: UserDB = Depends(get_current_user)
) -> List[OrderDB]:
    return await get_user_orders(db, user_id)


@router.get("/{user_id}/orders/{order_id}", response_model=OrderFullDB)
async def get_order(
        user_id: UUID,
        order_id: UUID,
        db: AsyncSession = Depends(async_db_session),
        current_user: UserDB = Depends(get_current_user)
) -> OrderFullDB:
    return await get_user_order(db, user_id, order_id)


@router.post("/{user_id}/orders", response_model=OrderFullDB)
async def create_order(
        user_id: UUID,
        order_item: OrderFullCreate,
        db: AsyncSession = Depends(async_db_session),
        current_user: UserDB = Depends(get_current_user)
) -> OrderFullDB:
    return await create_user_order(db, user_id, current_user.id, order_item)


@router.patch("/{user_id}/orders/{order_id}", response_model=OrderDB)
async def update_order(
        user_id: UUID,
        order_id: UUID,
        order_item: OrderUpdate,
        db: AsyncSession = Depends(async_db_session),
        current_user: UserDB = Depends(get_current_user)
) -> OrderDB:
    order = await order_api.get_order(db, order_id)
    await is_performer_or_customer(current_user, order)
    return await update_user_order(db, order_id, order_item)


@router.post("/{user_id}/orders/{order_id}/comments/", response_model=CommentDB)
async def create_comment(
        user_id: UUID,
        order_id: UUID,
        comment_item: CommentCreate,
        db: AsyncSession = Depends(async_db_session),
        current_user: UserDB = Depends(get_current_user)
) -> CommentDB:
    order = await order_api.get_order(db, order_id)
    await is_performer_or_customer(current_user, order)
    return await create_order_comment(db, current_user.id, order_id, comment_item)


@router.patch("/{user_id}/orders/{order_id}/comments/{comment_id}", response_model=CommentDB)
async def update_comment(
        user_id: UUID,
        order_id: UUID,
        comment_id: UUID,
        comment_item: CommentUpdate,
        db: AsyncSession = Depends(async_db_session),
        current_user: UserDB = Depends(get_current_user)
) -> CommentDB:
    order = await order_api.get_order(db, order_id)
    await is_performer_or_customer(current_user, order)
    return await update_order_comment(db, comment_id, comment_item)
