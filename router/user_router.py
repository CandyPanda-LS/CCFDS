from fastapi import APIRouter

from DTO.bank_account import BankAccountSchema
from DTO.user import UserSchema
from service.user_service import UserService

user_router = APIRouter()

user_service = UserService()


@user_router.get("/user/{user_id}", tags=["user"])
async def get_user(user_id: str):
    return await user_service.get_user(user_id)


@user_router.get("/user", tags=["user"])
async def get_users():
    users = await user_service.get_users()
    return users


@user_router.post("/user", tags=["user"])
async def create_user(user_data: UserSchema):
    user_obj = user_data.model_dump()
    return await user_service.create_user(user_obj)


@user_router.delete("/user", tags=["user"])
async def delete_user(user_id: str):
    return await user_service.delete_user(user_id)


@user_router.post("/user/{user_id}/account", tags=["user"])
async def create_bank_account(user_id: str, account_data: BankAccountSchema):
    account_obj = account_data.model_dump()
    return await user_service.create_bank_account(user_id, account_obj)


@user_router.delete("/user/{user_id}/{account_id}", tags=["user"])
async def delete_bank_account():
    return {"message": "Hello World"}
