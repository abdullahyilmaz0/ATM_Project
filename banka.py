import os
import random
import csv

hesaplar={ }
def olustur():
    global hesaplar
    ad =input("isminizi giriniz...:")
    soyad=input("soyadinizi giriniz...")
    bakiye=int(input("bakiye girisi yapiniz...:"))
    hn=f"{ad[0].upper()}{soyad[0].upper()}{random.randint(100000,999999)}"
    hesaplar[hn]={"ad": ad, "soyad": soyad, "bakiye": bakiye}

    
    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Hesap Numarası", "Ad", "Soyad", "Bakiye"])
    
        for hesap_no, bilgiler in hesaplar.items():
            writer.writerow([hesap_no, bilgiler["ad"], bilgiler["soyad"], bilgiler["bakiye"]])

    print("Hesap basariyla kaydedildi.")
    
    os.system('cls')
def görüntüle():
    print()
def bakiye_görüntüle():
    global hesaplar
    hesap_var_mi = input("Hesabınız var mı? (evet/hayir): ").lower()
    if hesap_var_mi == "evet":
        hesap_no = input("Hesap numaranızı giriniz...: ")
        if hesap_no in hesaplar:
            print(f"Bakiye: {hesaplar[hesap_no]['bakiye']} TL")
        else:
            print("Hesap numarası bulunamadı.")
    elif hesap_var_mi == "hayir":
        hesap_olusturmak = input("Hesap oluşturmak ister misiniz? (evet/hayir): ").lower()
        if hesap_olusturmak == "evet":
            ad = input("isminizi giriniz...: ")
            soyad = input("soyadinizi giriniz...: ")
            olustur(ad, soyad, 0)
            print("Yeni hesap oluşturuldu. Bakiye: 0 TL")
        else:
            print("Hesap oluşturma işlemi iptal edildi.")
    else:
        print("Geçersiz seçenek.")
    
    ana_menu()
def para_yatir():
    print()
def para_cek():
    print()
def transfer():
    print()
def exit():
    print()
os.system('cls')
print("""
1- Hesap Bilgileri Görüntüle
2- Bakiye Görüntüle
3- Para Yatirma
4- Para Cekme
5- Para Transferi
6- Hesap Olusturma
7- Cikis
 """)
sec=input("LÜtfen Islem Seciniz...:")
if sec == "1":
    görüntüle()
elif sec=="2":
    bakiye_görüntüle()
elif sec=="3":
    para_yatir()
elif sec=="4":
    para_cek()
elif sec=="5":
    transfer()
elif sec=="6":
    olustur()
elif sec=="7":
    exit()
    