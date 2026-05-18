from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column   
from sqlalchemy import func, DateTime
from datetime import datetime
import uuid
class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
