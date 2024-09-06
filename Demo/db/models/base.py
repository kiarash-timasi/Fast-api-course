from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=True, server_default=sa.text('now()'))