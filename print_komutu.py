

 print("Merhaba Dünya")
 # ÇIKTISI-> Merhaba Dünya
 print("Merhaba /tDünya")      # -> /t komutu tab tuşu görevi görür gibi boşluk bıraktırır.
 # ÇIKTISI-> Merhaba   Dünya 
 
 print("Merhaba \nDünya")      # -> \n komutu bir alt satırda yazdımak amacı ile kullanılır.
 # ÇIKTISI-> Merhaba
 #           Dünya
 
 print("kalem\tsıra\tsilgi")   #-> \t komutu 1 tane  tab görevi görür boşluk bırakır  
 # ÇIKTISI-> kalem	sıra	silgi
 
 ---- TYPE FONKSİYONU ---
 # type() fonksiyonu içine gönderilen verinin hangi veri tipinde olduğunu gösterir.
 
 -- ÖRNEK --
 a = 97
print(type(a))

# ÇIKTISI-> <class 'int'> -> int yani integer (tam sayı)
 -- ÖRNEK --
a = "fenerbagçe"
print(type(a))
 # ÇIKTISI->  <class 'str'> str yani string (yazı tipi)
 
 ---SEP PARAMETRESİ--- 
 # Yazdırdığımız değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar 
 --- ÖRNEK ---
 print("01","08","1997",sep="/")
 # ÇIKTISI-> 01/08/1997
 --- ÖRNEK ---
 print("FENERBAGÇE","BEŞİKTAŞ","GALATASARAY", sep= "\n")
 # ÇIKTISI-> FENERBAGÇE
 #           BEŞİKTAŞ
 #           GALATASARAY
 --- YILDIZ PARAMETRESİ ---
# Stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu strin karakterlerine ayrılacak ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır.
--- ÖRNEK ---
print(*"PYTHON")
# ÇIKTISI-> P Y T H O N 
--- ÖRNEK ---
print(*"PYTHON", sep= "\n")
  # ÇIKTISI->  P
  #            Y
  #            T
  #            H
  #            O
  #            N
  
  
  
  
  
  
  
  
