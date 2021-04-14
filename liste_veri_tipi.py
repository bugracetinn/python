#Stringlerden ayıran yönü Stringler direkt olarak değiştirilemez fakat listelerin içindeki karakterler değiştirilebilir

liste = ["Elma","35","Merhaba",3.14,5]
type(liste)
#ÇIKTISI -> list     -----> type() komutu verinin hangi tip de olduğunu gösterir.

-- VERİYİ LİSTEYE ÇEVİRME ---
->list komutu
ÖRNEK:
degisken = list("Merhaba")
print(degisken)
#ÇIKTISI -> ['M', 'e', 'r', 'h', 'a', 'b', 'a']

--- LİSTELERİ İNDEKSLEME VE PARÇALAMA ---
#LİSTELEMELER 0'DAN BAŞLAR.

ÖRNEK:
liste = [1,2,3,4,5,6,7]  
liste[0]
#ÇIKTISI -> 1
ÖRNEK:
liste = [1,2,3,4,5,6,7]
liste[2]
#ÇIKTISI -> 3
ÖRNEK:
liste = [1,2,3,4,5,6,7]
liste[-1] # -1 SONDAKİ VERİYİ GÖSTERİR VE -2,-3.. OLARAK DA İNDEKSLENİR.
#ÇIKTISI -> 7
liste[len(liste)-1] # LEN VERİYİ SAYAR 7 TANE VERİYİ BULUR VE 1 ÇIKARIRIRSAK DA  6'NCI İNDEKSİ BULMUŞ OLURUZ. 
#ÇIKTISI -> 7
--- PARÇAMALA----

ÖRNKEK:
liste = [1,2,3,4,5,6,7] 
liste[:5] # BAŞTAN BAŞLAR VE SONDAKİNİ DAHİL ETMEZ
#ÇIKTISI -> [1, 2, 3, 4, 5]
ÖRNEK:
liste = [1,2,3,4,5,6,7]
liste[1:5] # 1'DEN BAŞLAR 5'E KADAR GİDER AMA 5'İ ALMAZ
#ÇIKTISI-> [2, 3, 4, 5]

ÖRNKEK:
liste = [1,2,3,4,5,6,7] 
liste[::2] # BAŞTAN SONA KADAR GİT VE 2 ATLAYARAK GİT (BURDA İLK SAYIYI 1 KABUL EDER)
#ÇIKTISI -> [1, 3, 5, 7]
ÖRNEK:
liste = [1,2,3,4,5,6,7]
liste[1:5:2] # 1'DEN BAŞLA 5'KADAR GİT 2 ATALAYARAK GİT (5 DAHİL DEĞİL)
#ÇIKTISI -> [2, 4]
ÖRNEK:
liste = [1,2,3,4,5,6,7]
liste[::-1] # SONDAN BAŞA DOĞRU SIRALAR.
#ÇIKTISI -> [7, 6, 5, 4, 3, 2, 1]

--- LİSTELERDE İNDEKS İLE VERİ DEĞİŞTİRME ----
ÖRNEK:
liste=["fenerbahçe",19,"01"]     #!!!!!! 01 YAZARKEN "" İÇİNDE YAZMAK GEREKİR YOKSA EROR ALIRSINIZ.ONDALIK TAMSAYI DEĞİŞMEZLERİNDE ÖNDE GELEN SIFIRLARA İZİN VERİLMEZ;
liste[2]="07"  #!!! İNDEKSLERİN İLK VERİSİ SIFIR(0)'DAN BAŞLAR.
print(liste)
#ÇIKTISI-> ['fenerbahçe', 19, '07']
ÖRNEK:
liste = [1,2,3,4,5,6] 
liste[:2]
liste[:2] = [10,11] #BAŞTAN BAŞLA 2.İNDEKSE KADAR GİT 2'YE DAHİL ETME 2 VERİYİ [10,11] OLARAK DEĞİŞTİR.
print(liste)
#ÇIKTISI -> [10, 11, 3, 4, 5, 6]
----LEN KOMUTU ----
#LİSTE İÇİNDE VERİ SAYISINI BULMAK İÇİN KULLANILIR.
liste3 = [1,2,3,4,5,6,7,8]
len(liste3)
#ÇIKTISI -> 8
----- LİSTELERDE İŞLEMLER ----
-- TOPLAMA --
ÖRNEK:
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + liste2
print(liste3)
#ÇIKTISI [1, 2, 3, 4, 5, 6]
--- ÇARPMA ---
liste1 = [1,2,3]  
liste * 3   # SONRADAN liste1 PRİNT EDİLİRSE YİNE  [1,2,3] BU ÇIKTIYI VERİR SONRADAN YENİ ÇIKTI DEVAM ETMEZ  -> liste1 = liste1 * 3 bu şekilde yazılırsa sonra 
 #ÇIKTISI -> [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]                                             YENİ SONU ÇIKTI DEVAM EDER.                                      
---- APPEND KOMUTU -----
# VERİLEN DEĞERİ LİSTEYE EKLEMEK İÇİN KULLANILIR.
ÖRNEK:
liste = [3,4,5,6]
liste.append(7)
print(liste)
#ÇIKTISI -> [3, 4, 5, 6, 7]
liste.append("buğra")
print(liste)
[3, 4, 5, 6, 7, 'buğra']
---- POP METODU ----
# POP METODU İÇERİSİNE DEĞER VERİLMEZSE LİSTEDEKİ SON DEĞERİ,EĞER VERİLİRSE VERİLEN DEĞERİ LİSTEDEN ATAR VE ATILANI EKRANI GÖSTERİR
ÖRNEK:
liste = [1,2,3,4,5]
liste.pop()
5 # ÇIKARILAN ELAMAN
print(liste)
#ÇIKTISI-> [1, 2, 3, 4] 
ÖRNEK:
liste = [1,2,3,4,5]
liste.pop(1)
2 #ÇIKARILAN ELAMAN
#ÇIKTISI ->[1, 3, 4, 5]

----- SORT METODU ----
# LİSTENİN ELAMANLARINI SIRALAMAMIZI SAĞLAR
ÖRNEK:
liste = [1,2,3,4,5] #KÜÇÜKTEN BÜYÜĞE SIRALAR
liste.sort()
#ÇIKTISI -> [1, 2, 3, 4, 5]
ÖRNEK:
liste = [1,2,3,4,5]
liste.sort(reverse=TRUE)
print(liste)
#ÇIKTISI -> [5, 4, 3, 2, 1]  





