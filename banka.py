import os
import random
import csv
import re
import pandas as pd

hesaplar={ }

def olustur():
    global hesaplar, hn
    
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
    hesaplar={"Hesap Numarasi": hn, "ad": ad, "soyad": soyad, "bakiye": bakiye}
    csv_file='data.csv'
    if not os.path.isfile(csv_file):    # dosyanin önceden olusturulup olusturulmadugini kontrol etmek icin
        with open(csv_file, 'w', encoding='utf-8') as file_csv: # dosya yoksa yeniden olusturulup sütün adlari eklenir b    
            writer = csv.writer(file_csv)
            writer.writerow(["Hesap Numarası", "Ad", "Soyad", "Bakiye"])
        print(f'{csv_file} created.')
    else:
        print('File already exists.')
    
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)        
    
        for hesap_no, bilgiler in hesaplar.items():
            writer.writerow([hesap_no, bilgiler["ad"], bilgiler["soyad"], bilgiler["bakiye"]])

    print("Hesap basariyla kaydedildi.")
# Para çekme fonksiyonu
# def para_cek():
#     hesap_no = input("Hesap numaranızı giriniz: ")
#     if hesap_no in hesaplar:
#         while True:
#             miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
#             if hesaplar[hesap_no]['bakiye'] >= miktar:
#                 hesaplar[hesap_no]['bakiye'] -= miktar
#                 hesaplari_kaydet()  # Güncellenen bakiyeyi dosyaya kaydediyoruz
#                 print(f"{miktar} TL çekildi. Kalan bakiye: {hesaplar[hesap_no]['bakiye']} TL")
#                 break
#             else:
#                 print("Yetersiz bakiye. Lütfen geçerli bir miktar giriniz.")
#     else:
#         print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")
   
def para_cek():
    hesap_no = input("Hesap numaranızı giriniz: ").strip().upper()
    csv_file = 'data.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            if row[0] == hesap_no:
                while True:
                    miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
                    if int(row[3]) >= miktar:
                        new_bakiye = int(row[3]) - miktar
                        with open(csv_file, 'r+', encoding='utf-8') as file:
                            lines = file.readlines()
                            for i, line in enumerate(lines):
                                if line.startswith(hesap_no + ','):
                                    lines[i] = f"{hesap_no},{row[1]},{row[2]},{new_bakiye}\n"
                            file.seek(0)
                            file.writelines(lines)
                            file.truncate()
                        print(f"{miktar} TL çekildi. Kalan bakiye: {new_bakiye} TL")
                        break
                    else:
                        print("Yetersiz bakiye. Lütfen geçerli bir miktar giriniz.")
                break
        else:
            print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")

def input_valid_yazi(schreiber):    # Kullanicidan girilen degerlerin yazi olup olmadigini kontrol etmek icin
    while True:
        user_input = input(schreiber).strip().upper()

        if user_input.isalpha():
            return user_input
        else:
            print("Yanlış giriş! Lütfen sadece harf girin.\n")

def input_valid_sayi(zahl): # Kullanicidan girilen degerlerin sayi olup olmadigini kontrol etmek icin
    
    while True:
        phone = input(zahl).strip()

        if phone.isdigit():
            return phone
        else:
            print("Yanlış giriş! Lütfen sadece rakam girin.\n")

def input_valid_id():   # Kullanicidan girilen degerlerin belli bir karekter ve degere sahip olup olmadigini kontrol etmek icin
    pattern = r'^[A-Z]{2}\d{6}$'  # 2 harf (A-Z) ve 6 rakam (0-9)
    
    while True:
        phone = input("Görüntülenecek hesabın hesap numarasını giriniz (2 harf + 6 rakam, toplam 8 karakter): ").strip().upper()
        
        if re.match(pattern, phone):
            return phone
        else:
            print("Yanlış giriş! Hesap numarası 2 harf ve ardından 6 rakamdan oluşmalıdır.\n")

def control():  # Kullanicinin menüde kalip kalmayacagini kontrol etmek icin
    print("""
1- İşlemlere Devam Etmek
2- Ana Menüye Dönüş
 """)
    sec = input_valid_sayi("Lütfen İşlem Seçiniz...: ")
    if sec == "1":
        return True
    elif sec == "2":
        return False
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.\n")
        return control()

def goruntuleme():
    file_name = 'data.csv'
    
    try:
        df = pd.read_csv(file_name)  # CSV dosyasını pandas modulunde okur
        while True:
            query = input_valid_id()
            
            # Belirli hesap numarasını sorgulama
            print()
            result = df[df.apply(lambda row: query in row.astype(str).values, axis=1)]
            
            if not result.empty:
                print(result.to_string(index=False))
            else:
                print("Kayıt bulunamadı.\n")
            
            if not control():
                break
    except FileNotFoundError:
        print(f'{file_name} bulunamadı. Lütfen önce dosyayı oluşturun.\n')
    
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
# def para_cek():
#     print()
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
    
