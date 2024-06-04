# While döngüsü

i = 0
while i < 5:
    print("i'nin değeri:{}".format(i))
    i += 1

"""
Çıktı

i'nin değeri:0
i'nin değeri:1
i'nin değeri:2
i'nin değeri:3
i'nin değeri:4

"""

lists = [1, 2, 3, 4, 5]
for i in lists:
    print(i)

# Yukarıdaki for while ile kullanımı

index = 0
while index < len(lists):
    print(lists[index])
    index += 1

# Range fonksiyonu 0'dan 20'ye kadar sayı oluşturur
print(*range(0, 20))

# Çift sayıları 20'ye kadar olanları
print(*range(0, 20, 2))
# Tek sayıları 20'ye kadar olanları
print(*range(1, 20, 2))
# Tersten sıralama kullanımı
print(*range(20, 0, -1))

#for ile range fonksiyonunun kullanımı

for i in range(0, 20):
    print(i)


#Ters dik üçgen
for i in range(10, 0,-1):
    print("*" * i)

"""
Çıktı:

**********
*********
********
*******
******
*****
****
***
**
*

"""