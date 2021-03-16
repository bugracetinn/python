#DEĞİŞKENLERDE DİKKAT EDİLMESİ GEREKEN KURALLAR 

# Değişkenlere isim verirken  SAYI ile başlayan isimler verilmez ama harften sonra sayı kullanılabilir.(1degisken-> (Hata verir), degisken1->(kullanılabilir))
                       <----- ÖRNEK ---->
sayi = 10                     1sayi = 10
print(sayi)                   print(1sayi)
# çıktısı -> 10               # çıktısı -> EROR

* Değişkenlere isim verirken  BOŞLUK bırakarak  isimler verilmez. (degisken 1 -> hata verir)
* Değişkenlere isim verirken  "*(/ gibi karakterler verilmez. ( fakat _ bu karakter kullanılabilir)
* Rezerve edilmiş yazılarla isimlendirme yapılmaz örnek olarak degiskene print ismi verilmez çünkü print rezerve bir komuttur. 
* Eğer bir değişkene String (harf dizisi) kullanılcaksa "" işaretleri arasına yazılması gerekir.
                       <---- ÖRNEK--->
  a = 5                                                                    a = 5b
#çıktısı -> 5                                                          #çıktısı-> EROR ( Eğer eror almak istemiyorsanız a = "5b" şeklinde yazmanız gerekir)
( "" içinde değil ama eror vermez çünkü İnteger(tamsayı)'dır    AMA    
  



# <---- PRATİKLER ---->

x,y,z = "Masa", "Kalem", "Sıra"                       
print(x)
print(y)
print(z)                                                                                        x = y = z = "Masa"
#ÇIKTISI -> Masa         hepsini tek değişkene atamak istersek ->                                 print(x)
#           Kalem                                                                                 print(y)
 #          Sıra                                                                                  ptint(z)
  #                                                                                           ÇIKTISI -> Masa                
   #                                                                                                     Masa
    #                                                                                                    Masa


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
sehir ="İstanbul"
a = 10
b ="5"  
c = 2

print(sehir)                
print("Şehir: " + sehir)    
print(a + c)

ÇIKTISI -> İstanbul
           Şehir:İstanbul
           12



                                                                                                        
                                                                                                        

  
           
