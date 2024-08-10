from datetime import datetime

tespit = []
tespitSpe = [] # etnik karakter
tespit10 = [] # 10 karakterden fazla
karakter = []
tarama = 0
analizz = 0
tes10buy = 0
tesKal = 0
tesEtnik = 0
f = open("/media/mrblgn/716810b6-c64d-42e9-bb03-e4680b7a0066/rockfor2024/f5000_12.txt", "r")
for x in f:
    tarama += 1
    if tarama%500000 == 0:
        print("Tarama",tarama," At ",datetime.now())
    if tarama == 10000000:
        break
    tes10 = 0
    tesK = 0
    tesB = 0
    tesR = 0
    tesO = 0
    tesE = 0
    karakter.clear()
    axc = []
    axc = x
    if len(axc) > 9:
        tespit10.append(x)
        tes10 = 1
    for let in axc:
        if ord(let) > 96 & ord(let) < 124:
            #Küçük Harf
            tesK += 1
        if ord(let) > 64 & ord(let) < 92:
            #Büyük Harf
            tesB += 1
        if ord(let) > 32 & ord(let) < 49:
            # Özel karakter 1
            tesO += 1
        if ord(let) > 48 & ord(let) < 60:
            # Rakam
            tesR += 1
        if ord(let) > 192:
            #Etnik Harf
            tesE += 1
    karakter.append(tes10)
    karakter.append(tesK)
    karakter.append(tesB)
    karakter.append(tesR)
    karakter.append(tesO)
    karakter.append(tesE)
    tespit.append([karakter[0],karakter[1],karakter[2],karakter[3],karakter[4],karakter[5]])
    # İçeriyor mu?
    #print(x)
#print(tespit)
xx = 0
for x in tespit:
    if x[0] == 1:
        tes10buy += 1
    if x[5] > 0:
        tesEtnik += 1
print("Analiz Başlıyor: ",datetime.now())
print("Toplam incelenen şifre sayısı: ",len(tespit))
print("10 karakterden fazla şifre sayısı: ",tes10buy)
print("Etnik Karakterli Şifre Sayısı: ",tesEtnik)
# Büyük Harf: 65-91, küçük harf 97-123, özel harfler 193-351, özel karakter 33-48,  sayı: 49-59
# Büyük katf, küçük harf, rakam, özel karakter, en az 10
f.close()
tespit=[]
