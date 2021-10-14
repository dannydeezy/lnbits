from sqlite3 import Row
from fastapi.param_functions import Query
from pydantic import BaseModel
import time

class CreateCharge(BaseModel):
    onchainwallet: str = Query(None)
    lnbitswallet: str = Query(None)
    description: str = Query(...)
    webhook: str = Query(None)
    completelink: str = Query(None)
    completelinktext: str = Query(None)
    time: int = Query(..., ge=1)
    amount: int = Query(..., ge=1)

class Charges(BaseModel):
    id: str
    user: str
    description: str
    onchainwallet: str
    onchainaddress: str
    lnbitswallet: str
    payment_request: str
    payment_hash: str
    webhook: str
    completelink: str
    completelinktext: str
    time: int
    amount: int
    balance: int
    timestamp: int

    @classmethod
    def from_row(cls, row: Row) -> "Charges":
        return cls(**dict(row))

    @property
    def time_elapsed(self):
        if (self.timestamp + (self.time * 60)) >= time.time():
            return False
        else:
            return True

    @property
    def paid(self):
        if self.balance >= self.amount:
            return True
        else:
            return False
