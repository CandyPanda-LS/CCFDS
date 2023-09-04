from pydantic import BaseModel


class BankAccountSchema(BaseModel):
    account_number: str
    account_name: str
    bank_name: str
    bank_code: str
    bank_balance: float

    class Config:
        json_schema_extra = {
            "example": {
                "account_number": "1234567890",
                "account_name": "Savings",
                "bank_name": "GTB",
                "bank_code": "058",
                "bank_balance": 1000000.00
            }
        }