# Fonksiyon tanımlama

def information(name="No name", surname="No name"):
    print("Hello " + name + " " + surname)


information()
information("Mehmet", "ERÖZKAN")


# Faktoriyel hesaplama fonksiyonu
def fakto(n):
    faktoriyel = 1
    if n == 0 and n == 1:
        return 1
    for i in range(1, n + 1):
        faktoriyel *= i
    print(faktoriyel)


fakto(5)

"""
Çıktı

120
"""


# Recürsif fonksiyon

def FaktoRecursif(n):
    if n == 1:
        return n
    else:
        return n * FaktoRecursif(n - 1)


print(FaktoRecursif(5))


# Esnek parametre sayısı * ile tanımlanır
def toplam(*a):
    print(sum(a))


toplam(1, 2, 3, 4, 5, 6)


#Yerel ve Global değişkenler

#Yerel Değişken sadece function içinden erişilen değişkenler
def fonksiyon():
    a = 10
    print(a)

fonksiyon()


#Global Değişken funtion dışında tanımlanan değişkenlerdir

a = 10
def fonksiyon():
    print(a)

fonksiyon()


#Lambda ile fonksiyon tanımlama, küçük fonksiyonlar için kullanılır

kareAl = lambda x: x * x
print(kareAl(5))

topla = lambda *a : sum(a)
print(topla(1,2,3,4))
