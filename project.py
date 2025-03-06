ogrenciler = []

def menu():
    while True:
        print("\nÖğrenci Yönetim Sistemine Hoşgeldiniz!")
        print("1. Öğrenci Ekle")
        print("2. Öğrenci Bilgilerini Görüntüle")
        print("3. Belirli Öğrenciyi Görüntüle")
        print("4. Öğrenci Güncelle")
        print("5. Öğrenci Sil")
        print("6. Çıkış")

        secim = input("\nLütfen yapmak istediğiniz işlemi 1-6 arasında bir değer giriniz: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_goruntule()
        elif secim == "3":
            belirli_ogrenci_goruntule()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Programdan çıkılıyor......")
            break
        else:
            print("\nGeçersiz bir tuşlama yaptınız. Lütfen 1-6 arasında bir değer girin.")

def ogrenci_ekle():
    ad = input("\nÖğrenci Adını Girin: ")
    soyad = input("Öğrenci Soyadını Girin: ")
    numara = input("Öğrencinin Numarasını Girin: ")
    bolum = input("Öğrencinin Bölümünü Girin: ")
    not_ortalamasi = float(input("Öğrencinin Not Ortalamasını Girin: "))

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Numara": numara,
        "Bölüm": bolum,
        "not_ortalamasi": not_ortalamasi 
    }

    ogrenciler.append(ogrenci)
    print(f"\n{ad} {soyad} başarıyla eklendi!")

def ogrenci_goruntule():
    if not ogrenciler:
        print("\nListede öğrenci bulunmamaktadır.")
    else:
        print("\nTüm Öğrenciler:")
        for ogrenci in ogrenciler:
            print(f"Adı: {ogrenci['Ad']} {ogrenci['Soyad']}, Numarası: {ogrenci['Numara']}, Bölümü: {ogrenci['Bölüm']}, Not Ortalaması: {ogrenci['not_ortalamasi']}")

def belirli_ogrenci_goruntule():
    numara = input("\nÖğrenci numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print(f"Adı: {ogrenci['Ad']} {ogrenci['Soyad']}, Numarası: {ogrenci['Numara']}, Bölümü: {ogrenci['Bölüm']}, Not Ortalaması: {ogrenci['not_ortalamasi']}")
            return
    print("\nÖğrenci bulunamadı.")

def ogrenci_guncelle():
    numara = input("\nGüncellemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print("Mevcut Bilgiler:")
            print(f"Adı: {ogrenci['Ad']} {ogrenci['Soyad']}, Numarası: {ogrenci['Numara']}, Bölümü: {ogrenci['Bölüm']}, Not Ortalaması: {ogrenci['not_ortalamasi']}")
            
            ad = input("\nYeni Ad: ")
            soyad = input("Yeni Soyad: ")
            bolum = input("Yeni Bölümü: ")
            not_ortalamasi = float(input("Yeni Not Ortalaması: "))

            ogrenci["Ad"] = ad
            ogrenci["Soyad"] = soyad
            ogrenci["Bölüm"] = bolum
            ogrenci["not_ortalamasi"] = not_ortalamasi
            print(f"{ad} {soyad} bilgileri başarıyla güncellendi.")
            return
    print("\nÖğrenci bulunamadı.")

def ogrenci_sil():
    numara = input("\nSilmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            ogrenciler.remove(ogrenci)
            print(f"{ogrenci['Ad']} {ogrenci['Soyad']} başarıyla silindi.")
            return
    print("\nÖğrenci bulunamadı.")

menu()



