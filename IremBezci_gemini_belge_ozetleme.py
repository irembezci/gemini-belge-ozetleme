# 1. Gerekli kütüphaneleri içe aktar
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai


# 2. API anahtarını .env dosyasından oku
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY bulunamadı. .env dosyasını kontrol edin."
    )

client = genai.Client(api_key=api_key)


# 3. PDF içindeki metni oku
def read_pdf(pdf_path):

    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            print("PDF içerisinde okunabilir metin bulunamadı.")
            return None

        return text

    except FileNotFoundError:
        print("PDF dosyası bulunamadı.")
        return None

    except Exception as e:
        print(f"PDF okunurken hata oluştu: {e}")
        return None


# 4. PDF metnini Gemini modeline gönder ve Türkçe özet üret
def summarize_document(document_text):

    prompt = f"""
Aşağıdaki belgeyi Türkçe olarak özetle.

Yanıtı düz metin olarak ver.

Markdown kullanma.
#, ##, ### kullanma.
Kalın yazı kullanma.
Tablo kullanma.

Aşağıdaki başlıkları aynen kullan:

BELGENİN KISA AMACI

ANA MADDELER

ÖNEMLİ SONUÇLAR VEYA KARARLAR

DİKKAT EDİLMESİ GEREKEN NOKTALAR

Belge:
{document_text}
"""

    # 5. Model parametrelerini ayarla
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.2
        }
    )

    return response.text


# 6. Kullanıcıdan PDF dosya yolunu al
# 7. PDF oku
# 8. Özeti üret
# 9. Sonucu terminalde göster
def main():

    pdf_path = input("Özetlenecek PDF dosyasının adını giriniz:")

    document_text = read_pdf(pdf_path)

    if not document_text:
        return

    print("-" * 60)
    print("\nBelge başarıyla işlendi.")
    print("Türkçe özet hazırlanıyor...\n")
    print("-" * 60)

    summary = summarize_document(document_text)

    print("-" * 60)
    print("BELGE ÖZETİ")
    print("-" * 60)

    print(summary)

    print("-" * 60)


if __name__ == "__main__":
    main()
