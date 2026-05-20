from pydantic import BaseModel, Field
from typing import Literal
from decimal import Decimal
class MakeOperationWallet(BaseModel):
    operation_type: Literal['DEPOSIT', 'WITHDRAW'] = Field(...)
    amount: Decimal = Field(..., max_digits=20, decimal_places=2, gt=0)

class WalletBalance(BaseModel):
    balance: Decimal = Field(..., max_digits=20, decimal_places=2)