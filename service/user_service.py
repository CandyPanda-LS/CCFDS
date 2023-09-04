from http.client import HTTPException

from bson import ObjectId
from pymongo.errors import DuplicateKeyError

from database import user_collection, account_collection


class UserService:
    async def get_users(self):
        users = []
        async for user in user_collection.find():
            user_obj = dict(user)
            user_obj['_id'] = str(user_obj['_id'])

            for account in user_obj['bank_account']:
                account['_id'] = str(account['_id'])

            users.append(user_obj)
        return users

    async def create_user(self, user_data: dict):
        try:
            print(user_data)
            user = await user_collection.insert_one(user_data)
            return {'message': 'User registered successfully!'}
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail="Username already exists")
        except Exception as e:
            print(e)

    async def delete_user(self, user_id: str):
        user = await user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            await user_collection.delete_one({"_id": ObjectId(user_id)})
            return {'message': 'User deleted successfully!'}
        return HTTPException(status_code=400, detail="User does not exist")

    async def get_user(self, user_id: str):
        user = await user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user_obj = dict(user)
            user_obj['_id'] = str(user_obj['_id'])

            for account in user_obj['bank_account']:
                account['_id'] = str(account['_id'])

            return user_obj
        return HTTPException(status_code=400, detail="User does not exist")

    async def create_bank_account(self, user_id: str, account_data: dict):
        user = await user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            account = await account_collection.insert_one(account_data)
            user_collection.update_one({"_id": ObjectId(user_id)}, {"$push": {"bank_account": account_data}})
            return {'message': 'Account created successfully!'}
        return HTTPException(status_code=400, detail="User does not exist")

    async def delete_bank_account(self, user_id: str, account_id: str):
        user = await user_collection.find_one({"_id": user_id})
        if user:
            user_collection.update_one({"_id": user_id},  {"$pull": {"bank_account": {"_id": ObjectId(account_id)}}})
            return {'message': 'Account deleted successfully!'}
        return HTTPException(status_code=400, detail="User does not exist")