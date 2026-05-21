from models.wallet import Wallet
from .session import get_session
from uuid import UUID
import asyncio

async def seed():
    async_session_iterator = aiter(get_session())
    session = await anext(async_session_iterator)
    uuid1 = UUID('11111111111111111111111111111111')
    uuid2 = UUID('22222222222222222222222222222222')
    session.add(Wallet(id=uuid1))
    session.add(Wallet(id=uuid2))
    await session.commit()

if __name__ == '__main__':
    asyncio.run(seed())