from database import transactions_collection


class TransactionService:
    async def transaction_online(self, transaction: dict):
        try:
            transaction = await transactions_collection.insert_one(transaction)
            return {'message': 'Transaction created successfully!'}
        except Exception as e:
            print(e)

    async def transaction_pin(self, transaction: dict):
        try:
            transaction = await transactions_collection.insert_one(transaction)
            return {'message': 'Transaction created successfully!'}
        except Exception as e:
            print(e)
