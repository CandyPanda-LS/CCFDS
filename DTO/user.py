from typing import List

from pydantic import BaseModel

from DTO.bank_account import BankAccountSchema


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    dateofbirth: str
    phone: str
    address: str
    gender: str
    bank_account: List[BankAccountSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jhon@gmail.com",
                "password": "123456",
                "dateofbirth": "1998-12-12",
                "phone": "08123456789",
                "address": "Winstons place",
                "gender": "M",
                "bank_account": []
            }
        }

