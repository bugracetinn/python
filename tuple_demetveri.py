# Demetler veya ingilizce adıyla tuplelar listelere oldukça benzer ancak farkları demetlerin değiştililemez oluşudur. Bu yüzden programlarımızda değiştirilmesini
# istemediğimiz değerleri bir demet içinde depolayabiliriz.

demet = (1,2,3,4,5)
type(demet)
#ÇIKTISI -> tuple

--METODLAR--

--İndex metrodu--

--ÖRNEK--
demet=(1,2,3,4,5,6)
demet[4]
#ÇIKTISI -> 5

--Count metodu --
#tupleların içine verdiğimiz değerin kaç defa geçtiğini gösterir
--ÖRNEK--
demet=(1,1,1,1,2,2,4,5)
demet.count(1)
#ÇIKTISI -> 4
