from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

# Durum Geçmişi Şemaları
class ShipmentHistoryBase(BaseModel):
    status: str
    location: str

class ShipmentHistoryCreate(ShipmentHistoryBase):
    pass

class ShipmentHistoryResponse(ShipmentHistoryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True


# Kargo Gönderisi Şemaları
class ShipmentBase(BaseModel):
    sender_name: str = Field(..., example="Ahmet Yılmaz")
    receiver_name: str = Field(..., example="Ayşe Demir")
    receiver_address: str = Field(..., example="Kadıköy, İstanbul")
    weight_kg: float = Field(..., gt=0, example=2.5)

class ShipmentCreate(ShipmentBase):
    pass

class ShipmentStatusUpdate(BaseModel):
    status: str = Field(..., example="IN_TRANSIT")
    location: str = Field(..., example="Kadıköy Aktarma Merkezi")

class ShipmentResponse(ShipmentBase):
    id: int
    tracking_code: str
    status: str
    created_at: datetime
    history: List[ShipmentHistoryResponse] = []

    class Config:
        from_attributes = True