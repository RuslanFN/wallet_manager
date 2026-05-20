from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, ForeignKey, UUID
from .base import Base
from decimal import Decimal
from typing import TYPE_CHECKING
import uuid
if TYPE_CHECKING:
    from .user import User
class Wallet(Base):
    __tablename__ = 'wallets'
    balance: Mapped[Decimal] = mapped_column(
        Numeric(20, 2),
        default="0")

#   Я ПЕРЕДУМАЛ ДЕЛАТЬ ПОЛЬЗОВАТЕЛЯ
#    user_id: Mapped[uuid.UUID] = mapped_column(
#        UUID,
#        ForeignKey(User))
#    user: Mapped[User] = relationship(
#        User,
#        back_populates='wallets'
#    )
    
