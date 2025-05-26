from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    def __repr__(self) -> str:
        return "{name}({attrs})".format(
            name=self.__class__.__name__,
            attrs = ", ".join(
                f"{attr}={getattr(self, attr)}" for attr in self.__repr_attrs__
            ),
        )
        
        
class AssetRecord(Base):
    __tablename__ = "asset_records"
    __repr_attrs__ = ("id", "timestamp", "value")
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.now(datetime.UTC))
    value = Column(Float, nullable=False)