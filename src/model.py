from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    tracking_code = Column(String(32), unique=True, index=True, nullable=False)
    sender_name = Column(String(100), nullable=False)
    receiver_name = Column(String(100), nullable=False)
    receiver_address = Column(String(255), nullable=False)
    status = Column(String(50), default="ACCEPTED", nullable=False)
    weight_kg = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 1:N İlişki (Bir gönderinin birden çok hareket geçmişi olabilir)
    history = relationship("ShipmentHistory", back_populates="shipment", cascade="all, delete-orphan")


class ShipmentHistory(Base):
    __tablename__ = "shipment_history"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    status = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    shipment = relationship("Shipment", back_populates="history")