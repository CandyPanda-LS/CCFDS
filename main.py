from fastapi import FastAPI

from router.transaction_router import transaction_router
from router.user_router import user_router


app = FastAPI()

app.include_router(user_router)
app.include_router(transaction_router)


@app.get("/")
async def root():
    return {"message": "CCFD service"}
