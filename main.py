from models.transaction_models import TransactionIn, TransactionOut
from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/prueba")
    msg = "Metodo prueba"   
    return msg
