import os
import random
import csv

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
    hesap_no = input("Hesap numaranızı giriniz: ")
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
    
    os.system('cls')
def görüntüle():
    print()
def bakiye_görüntüle():
    print()
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
    
