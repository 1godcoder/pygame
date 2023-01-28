
#Seçiminizi Yazarken Baş Harfi Büyük Olsun

import random
secenek=["Taş","Kağıt","Makas"]
tas = secenek[0]
kagıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldinizn Oyunu bitirmek için q tuşuna basın")
while True:
    secim = input("Taş mı kağıt mı makas mı? ")
    bil_secim = random.choice(secenek)
    if secim==tas:
        if bil_secim==tas:
            print("Bilgisayarın seçimi: Taş Sonuç: Berabere")
        elif bil_secim==kagıt:
            print("Bilgisayarın seçimi: Kağıt Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç:Kazandınız")
    if secim==kagıt:
        if bil_secim==tas:
            print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
        elif bil_secim==kagıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç:Kaybettiniz")
    if secim==makas:
        if bil_secim==tas:
            print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
        elif bil_secim==kagıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç:Berabere")
        if secim == "q" or "Q":
            print("Çıkılıyor...")
            break