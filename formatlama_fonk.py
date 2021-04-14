#Programlama yapılırken bazı yerlerde bir string içinede daha öncesinden tanımlı stringifloat,,int vs yerleştirmek isteyebiliriz böyle durumlar için
#Pythonda format() fonksiyonunu  kullanabiliriz.

--- ÖRNEK ---
"{} {} {}" .format(2.345678,3.45678,6.78912) 
# ÇIKTISI-> '2.345678 3.45678 6.78912'

--- ÖRNEK ---
a = 3
b = 5
print("{}+{}'nin toplamı {}'dir".format(a,b,a+b))

# ÇIKTISI-> 3+5'nin toplamı 8'dir

--- ÖRNEK ---
# Süslü parantezlerin içindeki sayılar format fonkdiyonun içinden hagni sıradaki değerin geleceğini söylüyor.
"{1} {0} {2} ".format(19,"Fenerbahçe",'07')
# ÇIKTISI-> 'Fenerbahçe 19 07 '

--- ÖRNEK ---
# Süslü parantezlerin içindeki kullanım ondalıklı kısımın kaç basamak göstermek istediğimizi belirtir.
"{:.2f} {:.2f} {:.4f}".format(3.1234,4.1234,3.1234)
# ÇIKTISI-> '3.12 4.12 3.1234' 
