print("Market hesaplama programı başladı")

toplam = sepet_toplami()

urunler = {
    "elma": 12,
    "muz": 18,
    "süt": 35,
    "ekmek": 10
}

indirimli_urunler = ["elma", "süt", "peynir"

def sepet_toplami(urun_listesi):
    toplam = 0
    for urun, fiyat in urun_listesi.items():
        if fiyat > 20:
            print(urun, "pahalı ürün")
        else fiyat <= 20:
            print(urun, "uygun fiyatlı")
        toplam += fiyat
    return toplam

try:
    sonuc = sepet_toplami(urunler)
    print("Sepet toplamı:", sonuc)

while sonuc > 0
    sonuc -= 10
    print("Kalan:", sonuc)
    if sonuc == 20:
    print("Son 20 TL kaldı")

for urun in indirimli_urunler:
print("İndirimli ürün:", urun)

else:
    print("Döngü bitti")
