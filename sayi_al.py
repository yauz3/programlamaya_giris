# İki sayı ile bölme işlemi yapan örnek program

def sayi_al(mesaj):
    try:
        return float(input(mesaj))
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")
        return None

def bolme_yap(sayi1, sayi2):
    try:
        sonuc = sayi1 / sayi2
        return sonuc
    except ZeroDivisionError:
        print("Hata: Bir sayı 0'a bölünemez.")
        return None

def ana_program():
    print("Bölme programına hoş geldiniz.")
    
    sayi1 = sayi_al("Birinci sayıyı girin: ")
    if sayi1 is None:
        return
    
    sayi2 = sayi_al("İkinci sayıyı girin: ")
    if sayi2 is None:
        return
    
    sonuc = bolme_yap(sayi1, sayi2)
    if sonuc is not None:
        print("İşlem sonucu:", sonuc)

ana_program()
