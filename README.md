# Gemini ile Belge Özetleme

Bu proje, Türkiye Yapay Zeka Akademisi tarafından verilen LLM Ara Ödevi kapsamında geliştirilmiştir.

Amaç, Gemini API kullanarak PDF belgelerinin içeriğini okuyup Türkçe olarak özetleyen bir Python uygulaması geliştirmektir.

## Projenin Amacı

Bu çalışmada aşağıdaki konuların uygulamalı olarak öğrenilmesi hedeflenmiştir:

* Gemini API kullanımı
* API anahtarlarının güvenli yönetimi
* PDF dosyalarından metin çıkarma
* Prompt tasarımı ve yönlendirme
* Model parametrelerinin yapılandırılması
* Büyük Dil Modelleri (LLM) ile belge özetleme
* Terminal üzerinden kullanıcı etkileşimi
* Git ve GitHub ile proje yönetimi

## Projede Neler Yapıldı?

Uygulama aşağıdaki adımları gerçekleştirmektedir:

1. Kullanıcıdan PDF dosyasının adı veya yolu alınır.
2. PDF içerisindeki metin Python kullanılarak okunur.
3. Metin okunamazsa kullanıcıya hata mesajı gösterilir.
4. Belge içeriği Gemini modeline gönderilir.
5. Gemini, belgeyi Türkçe olarak özetler.
6. Oluşturulan özet terminalde düzenli bir formatta görüntülenir.

## Kullanılan Teknolojiler

* Python
* Gemini API
* google-genai
* python-dotenv
* pypdf
* Git
* GitHub

## Özet Çıktısı

Üretilen özet aşağıdaki bölümleri içermektedir:

* Belgenin Kısa Amacı
* Ana Maddeler
* Önemli Sonuçlar veya Kararlar
* Dikkat Edilmesi Gereken Noktalar

## Kurulum

Gerekli paketleri yüklemek için:

```bash
pip install -r requirements.txt
```

## .env Dosyası

Proje klasöründe `.env` isimli bir dosya oluşturulmalıdır.

Örnek:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Çalıştırma

```bash
python IremBezci_gemini_belge_ozetleme.py
```

Program çalıştırıldığında kullanıcıdan özetlenecek PDF dosyası istenir ve ardından Türkçe özet oluşturulur.

## Kazanımlar

Bu proje sayesinde:

* Gemini API ile çalışma deneyimi kazanıldı.
* PDF işleme süreçleri öğrenildi.
* Prompt tasarımı ve çıktı kontrolü uygulandı.
* LLM tabanlı belge özetleme uygulaması geliştirildi.
* GitHub üzerinde proje paylaşımı gerçekleştirildi.

## Türkiye Yapay Zeka Akademisi

Bu çalışma, Türkiye Yapay Zeka Akademisi LLM Ara Ödevi kapsamında hazırlanmıştır.
