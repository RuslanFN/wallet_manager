from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING, List
from .base import Base
if TYPE_CHECKING:
    from .wallet import Wallet
#class User(Base):
#    __tablename__ = 'users'
#    username: Mapped[str] = mapped_column(
#        String(50),
#        unique=True,
#        index=True)
#    hashed_password: Mapped[str]
    
#   ПОХОЖЕ ПО ТЗ ЭТО НЕ НУЖНО
#   wallets: Mapped[List[Wallet]] = relationship(
#       Wallet,
#       back_populates='user'
#       )
    
    