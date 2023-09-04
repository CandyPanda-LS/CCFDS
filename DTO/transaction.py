from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel

from DTO.bank_account import BankAccountSchema
from DTO.user import UserSchema


class TransactionSchema(BaseModel):
    category: str
    amount: float
    date: datetime
    retailer: str
    used_pin: bool
    used_online: bool
    user: str
    account: str

