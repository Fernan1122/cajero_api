from models.transaction_models import TransactionIn, TransactionOut
from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/user/balance/{username}")
    async def get_balance(username: str):
    '''user_in_db = get_user(username)'''
    '''if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())'''
    return username
