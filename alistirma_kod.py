
# Girilen metinde en uzun kelimeyi ve kaç harften oluştuğunu bulur
sentence = input("Cümle Girin: ")
longest = max(sentence.split(), key=len)
print("En uzun kelime: ", longest)
print("harf sayısı: ", len(longest))
################################################################################################################################################

