#Kaan Can ATEŞ - ACM 373 Final
#1.Soru
# Sayıları atıcağımız listeler tanımlanır
sayilar = []
list = []
liste = []
# Dosya okunur

with open("sayilar.txt","r") as sayi:
        # Sayıların olduğu alanları tek tek okuruz
        for line in sayi.readlines():
            # sayilar.append(line) alanın tamamını alır
            # Column numarası aralık olarak yazılır
            sayilar.append(int(line[11:14]))
            sayilar.sort()
sayi.close()
#2.Soru
for line in sayilar:
    # İlk en büyük sayıyı atarız
    list.append(sayilar[-1])
    toplam  = sayilar.pop()
    # 600'e tamamlayan küçük sayılar alınır
    while(toplam < 600):
        toplam2 = toplam + sayilar[0]
        # 600'ü geçmemesi sağlanır
        if  toplam2 < 600 :
            list.append(sayilar[0])
            toplam  += sayilar.pop(0)
        else:
            break
    # Array'e aktarılır
    liste.append(list)
    # Geçici array silinir
    list = []
print (liste)
