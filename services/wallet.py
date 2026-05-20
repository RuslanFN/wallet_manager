from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from models import Wallet
from decimal import Decimal
from typing import Coroutine
class WalletService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_wallet(self, uuid: UUID) -> Wallet | None:
        wallet = await self.session.get(Wallet, uuid)
        return wallet
    
    async def get_ballance(self, uuid: UUID) -> Decimal | None:
        wallet = await self.session.get(Wallet, uuid)
        if wallet:
            return wallet.balance
        return None
    
    async def make_operation_balance(
        self, 
        uuid: UUID,
        operation: str,
        amount: Decimal) -> Decimal | None:
        stmt = select(Wallet).where(Wallet.id == uuid).with_for_update()
        result = await self.session.execute(stmt)
        target_wallet = result.scalar_one_or_none()
        if target_wallet:
            if operation == 'WITHDRAW':
                target_wallet.balance -= amount
                if target_wallet.balance >= 0:
                    await self.session.commit()
                    return target_wallet.balance
                raise ValueError('NotEnoughMoney')
            elif operation == 'DEPOSIT':
                target_wallet.balance += amount
                await self.session.commit()
                return target_wallet.balance
            else:
                raise ValueError('InvalidOperation')
        else: 
            raise ValueError('NotFoundWallet')
        
   