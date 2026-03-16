def ana():
    sayac = 0
    toplam = 0
    while sayac < 3:
        try:
            sayi = int(input("Bir sayı girin: "))
            toplam += sayi
            sayac += 1
        except ValueError:
            print("Hata: Lütfen tam sayı girin.")
    print("Girilen sayıların toplamı:", toplam)

ana()
print("Program bitti.")
print("Teşekkürler.")
print("Yine bekleriz.")
