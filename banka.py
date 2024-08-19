import os
import random
import csv

hesaplar={ }
def olustur():
    global hesaplar
    
    while True:
        try:
            ad =str(input("isminizi giriniz...:"))           
            soyad=str(input("soyadinizi giriniz..."))
            bakiye = int(input("Lütfen bakiye girisi yapiniz...: "))
            break
        except ValueError:
            print("Lütfen sadece rakam kullanin !")
            continue
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
    print()
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
    