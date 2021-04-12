#LİSTELEME YÖNYEMİ YAZIMI  
meyveler = ["elma","portakal","muz"]
print(meyveler)

#ÇIKTI ['elma', 'portakal', 'muz']

    
#TUPLE YÖNTEMİ YAZIMI   
meyveler = ("elma","portakal","muz")
print(meyveler)

#ÇIKTISI
('elma', 'portakal', 'muz')

#Listenin elemanlarını değiştirebilirsin. Tuple'ın değiştiremezsin. Haliyle tuple daha az bellek harcar ve listeye göre daha kısa sürede iş yapar. 

#LİSTELEME YÖNTEMİNDE EKLEME
meyveler = ["elma","portakal","muz"]
print(meyveler)
#ÇIKTI: ['elma', 'portakal', 'muz']
meyveler[0] = "armut"
print(meyveler)
#ÇIKTI:['armut', 'portakal', 'muz']

#TUPLE YÖNTEMİ İLE EKLEME YAPACAK OLURSAK (Sondaki eror görülür)
meyveler = ("elma","portakal","muz")
print(meyveler)
#ÇIKTISI 
('elma', 'portakal', 'muz')
meyveler[0] = "armut"
# TypeError                                 Traceback (most recent call last)
#<ipython-input-77-9f594cadf180> in <module>
#----> 1 meyveler[0] = "armut"

#TypeError: 'tuple' object does not support item assignment  ->Şeklinde eror verir.
