
ogrenciler=[]

# Listeye Tek Bir  Öğrenci Ekleme
def OgEkle(adSoyad):
    adSoyad= input("Eklemek İstediğiniz Kişinin Adını ve Soyadını Aralarında Boşluk Olmadan  Giriniz :")
    ogrenciler.append(adSoyad)
    print (adSoyad + " isim ve soy isimli öğrenci listeye eklendi.")

# Listeye Birden Fazla Öğrenci Ekleme
def CokluOgEkleme(eklemeSayisi):
    i=0
    while i<eklemeSayisi:
        adSoyad=input("Eklemek İstediğiniz Kişinin Adını ve Soyadını Aralarında Boşluk Olmadan  Giriniz :")
        ogrenciler.append(adSoyad)
        i+=1
    return ogrenciler    

# Listeden Birden Fazla Öğrenci Silme
def ogSil (SilinecekOgrenci):
    SilinecekOgrenci = int(input("Silmek İstediğiniz Öğrenci Adedi : "))
    i =0
    while (i < SilinecekOgrenci):
        ogSil = input("Silmek İstediğiniz Kişinin Adını ve Soyadını Aralarında Boşluk Olmadan  Giriniz :")
        ogrenciler.remove(ogSil)
        i +=1
        return ogrenciler
    
# Listedeki  Öğrencinin İndex Numarasını Öğrenme 
def ogrNoOgrenme():
    OgrAdSoyad=input("Lutfen Numarasını Öğrenmek İstediğiniz Öğrencinin İsmini ve Soyismini  Aralarında Bir Boşluk Olmadan Giriniz : ")
    for OgrAdSoyad in ogrenciler:
        if OgrAdSoyad==ogrenciler:
            print(f"{OgrAdSoyad} İsimli Öğrencinin Numarası {ogrenciler.index(OgrAdSoyad)}")
        else : print("Öğrenci Listesinde Bu İsimde Bir Öğrenci Bulunmamaktadır.")

# Listedeki Ögrenci İsmini Silme
def Degistime():
    adSoyad=input("İstediğiniz Kişinin Adını ve Soyadını Aralarında Boşluk Olmadan  Giriniz :")
    for ogr in ogrenciler:
        if ogr==adSoyad:
            ogrenciler.remove(ogr)
            print(adSoyad + " isimli Öğrenci listeden Silindi") 
        else: 
            print ("Bu İsimde Öğrenci Bulunmamaktedır.")

# Öğrenci Listesi Yazdırma
def ogListeGoster():
    for i in range(len(ogrenciler)):
        print(ogrenciler[i])
   







    