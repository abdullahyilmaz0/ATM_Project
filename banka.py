import os
import random
import csv
import time
import sys
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
                        time.sleep(3)
                        break
                    else:
                        print("Yetersiz bakiye. Lütfen geçerli bir miktar giriniz.")
                break
        else:
            print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")
    
    os.system('cls')
def görüntüle():
    print()
def bakiye_görüntüle():
    hesap_no = input("Hesap numaranızı giriniz: ").strip().upper()  # Kullanıcıdan hesap numarasını al
    
    csv_file = 'data.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:# Dosyayı oku
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        
        for row in reader:# Her satırı kontrol ediyoruz
            if row[0] == hesap_no:  # Hesap numarası ile eşleşen satır bulunduğunda
                print(f"Hesap Numarası: {row[0]}\nAd: {row[1]}\nSoyad: {row[2]}\nBakiye: {row[3]} TL")
                time.sleep(2)
                break
        else:
            # Hesap numarası bulunamadıysa mesaj göster
            print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")
            time.sleep(2)

def para_yatir():
    hesap_no = input("Hesap numaranızı giriniz: ").strip().upper()
    csv_file = 'data.csv'
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        for row in reader:
            if row[0] == hesap_no:
                while True:
                    try:
                        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
                        if miktar <= 0:
                            print("Lütfen pozitif bir miktar giriniz.")
                            continue
                        new_bakiye = int(row[3]) + miktar  # Bakiyeye ekleme yapılıyor
                        with open(csv_file, 'r+', encoding='utf-8') as file:
                            lines = file.readlines()
                            for i, line in enumerate(lines):
                                if line.startswith(hesap_no + ','):
                                    lines[i] = f"{hesap_no},{row[1]},{row[2]},{new_bakiye}\n"
                            file.seek(0)
                            file.writelines(lines)
                            file.truncate()
                        print(f"{miktar} TL yatırıldı. Yeni bakiye: {new_bakiye} TL")
                        
                        break
                    except ValueError:
                        print("Lütfen geçerli bir miktar giriniz.")
                break
        else:
            print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")
    
    os.system('cls')

    print()
# def para_cek():
#     print()
def transfer():
    csv_file = 'data.csv'
    
    gonderen_hesap_no = input("Gönderen hesap numaranızı giriniz: ").strip().upper()
    alici_hesap_no = input("Alıcı hesap numarasını giriniz: ").strip().upper()
    
    try:
        # Hesapları yükle
        with open(csv_file, 'r', encoding='utf-8') as file:
            hesaplar = {row[0]: {'ad': row[1], 'soyad': row[2], 'bakiye': int(row[3])} 
                        for row in csv.reader(file) if row[0] != "Hesap Numarası"}
        
        # Gönderen ve alıcı hesap kontrolü
        if gonderen_hesap_no in hesaplar and alici_hesap_no in hesaplar:
            miktar = int(input("Transfer etmek istediğiniz miktarı giriniz: "))
            if 0 < miktar <= hesaplar[gonderen_hesap_no]['bakiye']:
                # Transfer işlemi
                hesaplar[gonderen_hesap_no]['bakiye'] -= miktar
                hesaplar[alici_hesap_no]['bakiye'] += miktar
                
               
                with open(csv_file, 'w', newline='', encoding='utf-8') as file: # Dosyayı güncelle
                    writer = csv.writer(file)
                    writer.writerow(["Hesap Numarası", "Ad", "Soyad", "Bakiye"])
                    writer.writerows([[no, bilgiler['ad'], bilgiler['soyad'], bilgiler['bakiye']] 
                                      for no, bilgiler in hesaplar.items()])
                
                print(f"{miktar} TL transfer edildi. Gönderen yeni bakiye: {hesaplar[gonderen_hesap_no]['bakiye']} TL, "
                      f"Alıcı yeni bakiye: {hesaplar[alici_hesap_no]['bakiye']} TL")
            else:
                print("Yetersiz bakiye veya geçersiz miktar.")
        else:
            print("Gönderen veya alıcı hesap numarası bulunamadı.")
    
    except FileNotFoundError:
        print(f"{csv_file} dosyası bulunamadı.")
    except ValueError:
        print("Lütfen geçerli bir miktar giriniz.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    print()
def exit():
    print("Programdan çıkılıyor...")
    time.sleep(2)
    sys.exit()  # Programı sonlandırır
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
    
