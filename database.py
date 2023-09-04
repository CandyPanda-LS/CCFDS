import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://root:root@cluster0.uav972i.mongodb.net/?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.CCFDS
user_collection = database.get_collection("users")
transactions_collection = database.get_collection("transactions")
account_collection = database.get_collection("accounts")