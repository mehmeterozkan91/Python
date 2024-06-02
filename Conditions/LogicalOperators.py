#Mantıksal Operatörler

# bool değeri
isZero = bool(5)
print(isZero)

# bool değeri 0 veya 0.0 ise sonuç False olur, 0 dan farklı ise True döner
isZero = bool(0)
print(isZero)
isZero = bool(0.0)
print(isZero)

# None değeri atama null yani sonradan atanacak anlamına gelir
a = None
print(a)
a = 5
print(a)

# Karşılaştırma operetörleri

# == eşittir operatörü
b = (1 == 1)
print("eşittir", b)

# != eşit değildir operatörü
b = ("Mehmet" != "ERÖZKAN")
print("eşit değildir", b)

# < küçüktür operatörü
b = ([1,2] < [1])
print("küçüktür", b)

# > büyüktür operatörü
b = (1 > 1)
print("büyüktür", b)

# <= küçük eşittir operatörü
b = (1 <= 1)
print("küçük eşittir ", b)

# >= büyük eşittir operatörü
b = (1 >= 1)
print("büyük eşittir", b)
