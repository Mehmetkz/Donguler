import random
sayi = random.randint(1,50)
hak = 5
print("Sayı tahmini")
while(hak>0):
    tahmin = int(input("Bir sayi giriniz"))
    if sayi < tahmin:
        print("Tahmin sayıdan buyuktur")
        hak -= 1
    elif sayi > tahmin:
        print("Tahmin sayidan kucuktur")
        hak -= 1
    elif sayi == tahmin:
        print("Doğru tahmin")
        break
if hak == 0:
    print("Tahmin hakkınız bitti")
    print(f"Tahmin etmeye çalıştığınız sayi {sayi}")


# Atm Uygulaması
kullanıcı_adı = "snape"
sifre = "56789"
bakiye = 100

ad = input("isim:")
sifre = input("sifre:")
if (ad == kullanıcı_adı) & (sifre == sifre):
    print("Hoşgeldiniz")
    while True:
        islem = input("isleminizi seciniz:")
        if islem == "1":
            tutar = int(input("yatırılan tutarı giriniz:"))
            bakiye += tutar
            break
        elif islem == "2":
            tutar = int(input("çekilen tutarı giriniz:"))
            if bakiye > tutar:
                bakiye -= tutar
                print(f"Kalan bakiyeniz: {bakiye}")
                break
            else:
                print("Bakiye yetersiz")
        else:
            print("Tanımlanamayan işlem")
            break
else:
    print("Yanlış sifre veya kullanıcı adı")

# Havuz problemi
def havuz(a,b):
    doldur = 0
    for i in range(len(a)):
        doldur = doldur + (1/a[i])
    bosalt = 0
    for i in range(len(b)):
        bosalt = bosalt + (1/b[i])
    if doldur-bosalt > 0:
        print("Havuz dolar")
    else:
        print("Havuz dolmaz")

a = [10,20,2,4]
b = [4,5,10,20]
havuz(a,b)

# Global Değişken Oluşturma
def topla(a,b):
    global toplam # global değişken tanımlama
    toplam = a+b
    return toplam
topla(3,4)
toplam

def rastgele():
    import random
    return (random.sample(range(1,50),3))
rastgele()

# Belirli sayıda random dizi oluşturma
def liste_sira(time,x,y,z):
    def liste():
        import random
        return (random.sample(range(x,y),z))
    for i in range(0,time):
        a = "liste_" + str(i+1)
        b = liste()
        print(f"{a} -> {b}")

liste_sira(5,1,10,5)

# Büyük ünlü uyumu bulma
def bul(string):
    sesli = ["a","e","i","ı","o","ö","u","ü"]
    kalin = ["a","ı","o","u"]
    ince = ["e","i","ö","ü"]
    kelime = string.split(sep = " ")
    uyan = []
    uymayan = []
    tek_hece = []


    for i in range(len(kelime)):
        icindeki_sesli = []
        for j in range(len(kelime[i])):
            if kelime[i][j] in sesli:
                icindeki_sesli.append(kelime[i][j])
        if len(icindeki_sesli) == 1:
            print(f"{kelime[i]} unlu uyumu yoktur.")
        else:
            if list(icindeki_sesli)[0] in kalin:
                if set(icindeki_sesli).issubset(set(kalin)):
                    uyan.append(kelime[i])
                else:
                    uymayan.append(kelime[i])
            else:
                if set(icindeki_sesli).issubset(set(ince)):
                    uyan.append(kelime[i])
                else:
                    uymayan.append(kelime[i])
    print(f"uyan kelime sayısı {len(uyan)}, uymayan kelime sayısı{len(uymayan)},tek heceli kelime sayısı {len(tek_hece)}")

    bul("deneme")