# Sistem Mimarisi ve Veri Modeli

## 1. Uygulama Mimarisi
Uygulama, FastAPI tabanlı katmanlı mimari (Layered Architecture) prensiplerine göre tasarlanmıştır:
- **API Rotaları (`src/main.py`):** Dış dünyaya açık REST uç noktaları.
- **Doğrulama Katmanı (`src/schemas.py`):** Pydantic tabanlı DTO (Data Transfer Object) modelleri.
- **İş Mantığı Katmanı (`src/crud.py`):** Veritabanı sorguları ve iş akışı kontrolleri.
- **Veri Kalıcılığı Katmanı (`src/database.py`, `src/models.py`):** SQLAlchemy ORM ve SQLite motoru.

## 2. Temel Veri Modeli
### Shipment (Kargo Gönderisi) Tablosu
- `id` (Integer, Primary Key)
- `tracking_code` (String, Unique, Index): TR-YYYYMM-XXXXX formatında benzersiz takip numarası.
- `sender_name` (String): Gönderici adı soyadı.
- `receiver_name` (String): Alıcı adı soyadı.
- `receiver_address` (String): Teslimat adresi.
- `status` (String): Kargonun anlık durumu (ACCEPTED, IN_TRANSIT, DELIVERED vb.).
- `weight_kg` (Float): Paket ağırlığı.
- `created_at` (DateTime): Kayıt oluşturulma zamanı.

### ShipmentHistory (Hareket Logları) Tablosu (1:N İlişki)
- `id` (Integer, Primary Key)
- `shipment_id` (Integer, ForeignKey to shipment.id)
- `status` (String): O anki durum.
- `location` (String): İşlemin yapıldığı merkez/şube.
- `timestamp` (DateTime): İşlem saati.