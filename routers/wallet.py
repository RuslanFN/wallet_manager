from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from services import WalletService
from schemas import MakeOperationWallet, WalletBalance
from db import get_session
router = APIRouter()

@router.get("/wallet/{uuid}", response_model=WalletBalance)
async def get_balance(uuid: str, session=Depends(get_session)):
    '''Возвращает баланс в Decimal'''
    service = WalletService(session)
    balance_or_None = await service.get_ballance(uuid)
    if balance_or_None is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",   
        )
    return {'balance':balance_or_None}

@router.post("/wallet/{uuid}/operation", response_model=WalletBalance)
async def make_operation(
    uuid: str,
    data: MakeOperationWallet,
    session=Depends(get_session)):
    '''Пополняет баланс и возвращает баланс в Decimal'''
    service = WalletService(session)
    balance_or_None = None
    try:
        balance_or_None = await service.make_operation_balance(uuid, data.operation_type, data.amount)
    except ValueError as e:
        if str(e) == "NotFoundWallet":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{e}",   
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",   
        )
    return {'balance':balance_or_None}
