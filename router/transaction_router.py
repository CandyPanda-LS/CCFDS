from fastapi import APIRouter

from DTO.transaction import TransactionSchema
from service.fraud_detection_service import FraudDetectionService
from service.transaction_service import TransactionService

transaction_router = APIRouter()
fraud_detection_service = FraudDetectionService()

transaction_service = TransactionService()

@transaction_router.post("/transaction/online", tags=["transaction"])
async def transaction_online(transaction: TransactionSchema):
    transaction_obj = transaction.model_dump()
    return await transaction_service.transaction_online(transaction_obj)


@transaction_router.post("/transaction/pin", tags=["transaction"])
async def transaction_pin(transaction: TransactionSchema):
    transaction_obj = transaction.model_dump()
    return await transaction_service.transaction_pin(transaction_obj)
