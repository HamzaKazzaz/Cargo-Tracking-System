import subprocess

tasks = [
    {
        "title": "Task #02: Yazılım Mimarisi ve Veri Modeli Tasarımı",
        "body": "### Task Description\nSQLite üzerinde çalışacak gönderi (Shipment) ve hareket logları (ShipmentHistory) tablolarının modellenmesi ve docs/architecture.md hazırlanması.\n\n### Acceptance Criteria\n- [ ] ER diyagramı ve veri modeli hazırlandı.\n- [ ] SQLAlchemy model sınıfları ve Pydantic şemaları oluşturuldu.\n- [ ] docs/architecture.md dosyası dokümante edildi.\n\n### Evidence\ndocs/architecture.md commit bağlantısı."
    },
    {
        "title": "Task #04: Gönderi Oluşturma Fonksiyonu (POST /shipments)",
        "body": "### Task Description\nYeni kargo kaydı oluşturan ve benzersiz takip kodu üreten endpoint'in kodlanması.\n\n### Acceptance Criteria\n- [ ] Pydantic girdi validasyonu yapıldı.\n- [ ] Takip kodu otomatik üretildi, statü ACCEPTED atandı.\n- [ ] Swagger üzerinden 201 Created yanıtı doğrulandı.\n\n### Evidence\nSwagger ekran görüntüsü ve commit hash."
    },
    {
        "title": "Task #05: Takip Kodu ile Kargo Sorgulama (GET /shipments/{code})",
        "body": "### Task Description\nTakip numarası ile anlık durum ve geçmiş hareketleri getiren servisin yazılması.\n\n### Acceptance Criteria\n- [ ] Takip koduna göre ilişkili geçmiş logları döndürüldü.\n- [ ] Bulunamayan kayıtlar için 404 Not Found döndürüldü.\n\n### Evidence\nAPI yanıt çıktısı."
    },
    {
        "title": "Task #06: Gönderi Durumu Güncelleme (PATCH /shipments/{code}/status)",
        "body": "### Task Description\nKargo durumunu güncelleyen ve ShipmentHistory tablosuna log düşen servisin kodlanması.\n\n### Acceptance Criteria\n- [ ] Geçerli durum geçişleri doğrulandı.\n- [ ] Zaman damgalı hareket kaydı veritabanına eklendi.\n\n### Evidence\nVeritabanı log kaydı ve HTTP 200 çıktısı."
    },
    {
        "title": "Task #07: Gönderi Listeleme ve İptal Servisleri",
        "body": "### Task Description\nKargoları filtreleyerek listeleyen ve uygun statüdeki kargoyu iptal eden servislerin yazılması.\n\n### Acceptance Criteria\n- [ ] Statüye göre filtreleme çalıştı.\n- [ ] Dağıtıma çıkmış kargonun silinmesi engellendi.\n\n### Evidence\nAPI sorgu çıktıları."
    },
    {
        "title": "Task #08: Git Flow ile Feature Branch ve Pull Request Yönetimi",
        "body": "### Task Description\nYeni özelliklerin feature branch'lerde geliştirilip PR ile main'e birleştirilmesi.\n\n### Acceptance Criteria\n- [ ] En az 2 ayrı feature branch açıldı.\n- [ ] Pull Request açılarak merge edildi.\n\n### Evidence\nKapatılan PR bağlantıları ve git graph çıktısı."
    },
    {
        "title": "Task #09: Pytest ile Otomatik Birim Testlerinin Yazılması",
        "body": "### Task Description\nUygulamanın temel fonksiyonları için en az 3 adet birim testinin kodlanması.\n\n### Acceptance Criteria\n- [ ] En az 3 adet unit test yazıldı.\n- [ ] Testler izole test veritabanında başarıyla geçti.\n\n### Evidence\nTerminal pytest -v çalıştırma logu."
    },
    {
        "title": "Task #10: GitHub Actions ile CI Pipeline Kurulumu",
        "body": "### Task Description\nPush ve PR anında testleri otomatik koşan .github/workflows/ci.yml pipeline'ının kurulması.\n\n### Acceptance Criteria\n- [ ] Bağımlılıklar pipeline içinde yüklendi.\n- [ ] pytest otomatik çalıştırıldı ve yeşil build alındı.\n\n### Evidence\nGitHub Actions run bağlantısı."
    },
    {
        "title": "Task #11: Dockerfile ve Konteyner İmajı Hazırlanması",
        "body": "### Task Description\nFastAPI uygulamasının bağımsız çalışması için Dockerfile hazırlanması ve imaj derlenmesi.\n\n### Acceptance Criteria\n- [ ] Dockerfile yazıldı.\n- [ ] Konteyner 8000 portundan başarıyla çalıştırıldı.\n\n### Evidence\ndocker build ve docker ps çıktıları."
    },
    {
        "title": "Task #12: Cloud PaaS Platformu Seçimi ve Dağıtımı",
        "body": "### Task Description\nUygulamanın Render/Railway gibi bir bulut platformuna deploy edilmesi.\n\n### Acceptance Criteria\n- [ ] Bulut servisinde proje ayağa kalktı.\n- [ ] Canlı URL üzerinden API yanıt verdi.\n\n### Evidence\nCanlı bulut API adresi."
    },
    {
        "title": "Task #13: CD Pipeline, Health Check ve Merkezi Loglama",
        "body": "### Task Description\nOtomatik deployment adımı, /health servisi ve izleme loglarının yapılandırılması.\n\n### Acceptance Criteria\n- [ ] /health servisi HTTP 200 verdi.\n- [ ] Bulut log panosu doğrulandı.\n\n### Evidence\nHealth check çıktısı ve canlı log ekranı."
    }
]

for t in tasks:
    cmd = [
        "gh", "issue", "create",
        "--repo", "HamzaKazzaz/Cargo-Tracking-System",
        "--title", t["title"],
        "--body", t["body"]
    ]
    subprocess.run(cmd)
    print(f"Basarili: {t['title']}")