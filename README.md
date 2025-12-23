# Pygame Demo Projesi – Top Yakalama Oyunu

Bu proje, Python Programlama dersi kapsamında hazırlanmış bir **Pygame demo oyunudur**. Amaç, Pygame kütüphanesinin temel oyun mekaniği özelliklerini (oyun döngüsü, giriş kontrolü, çarpışma, skor, can sistemi vb.) pratik olarak göstermektir.

## Projenin Amacı

Bu demo ile:
- Pygame kullanarak bir oyun penceresi oluşturma,
- Klavye ile oyuncu nesnesini (platform) hareket ettirme,
- Ekranın üstünden aşağı düşen bir topu takip etme,
- Çarpışma algılama (top–platform çarpışması),
- Skor ve can sistemi oluşturma,
- Kaçırma durumunda ekranda görsel geri bildirim (kırmızı yanma efekti),
- Oyun bittiğinde “OYUN BITTI” mesajı gösterme

gibi temel oyun programlama kavramları uygulanmaktadır.

## Oyun Mekaniği

- Oyuncu, ekranın alt kısmındaki **mavi dikdörtgen platformu** sağı–sol yön tuşları ile hareket ettirir.
- Ekranın üst kısmından **kırmızı bir top** aşağı doğru düşer.
- **Top platforma çarparsa:**
  - Skor 1 artar.
  - Top tekrar yukarıdan rastgele bir x konumunda başlar.
- **Top platforma değmeden ekranın altından çıkarsa:**
  - Oyuncunun **canı 1 azalır**.
  - Ekran kısa süreli **koyu kırmızı** renge döner (miss efekti).
  - Top yine yukarıdan rastgele bir konumda yeniden başlatılır.
- Oyuncunun başlangıçta **3 canı** vardır.
- Canlar 0 olduğunda:
  - Oyun durur.
  - Ekranda **“OYUN BITTI”** ve altında bilgilendirme metni gösterilir.
  - Pencereyi kapatarak oyun sonlandırılır.


## Proje Dosyaları

Proje klasör yapısı:

```text
Demo_Projesi/
│
├─ main.py            → Oyunun tüm Pygame kodları
├─ requirements.txt   → Gerekli Python kütüphanesi (pygame)
└─ README.md          → Proje açıklama dosyası (bu dosya)
```

---

## Nasıl Çalıştırılır

Bu demo proje, Python ve Pygame kullanılarak geliştirilmiştir. Projenin çalıştırılabilmesi için aşağıdaki adımların sırasıyla uygulanması gerekmektedir.

1. Bilgisayarınızda **Python 3.x** sürümünün kurulu olduğundan emin olun.

2. Proje klasörünü açın ve terminali (Komut İstemi / PowerShell / VS Code Terminal) bu klasör içerisinde çalıştırın.

3. Gerekli Python kütüphanelerini yükleyin:
```bash
pip install -r requirements.txt
```

4. Kütüphaneler yüklendikten sonra oyunu çalıştırmak için aşağıdaki komutu girin:
```bash
python main.py
```

-**Sevdenur Aktürk**

