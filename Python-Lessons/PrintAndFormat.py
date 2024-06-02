# Print fonksiyonu
print("Hello World")
print(3.14)
print("Hello World", 45, 3.14)

# \n karakteri alt alta yazdırmak istersek kullanılır
print("Hello World \nMehmet")

# \t karakteri boşluk bırakmak istersek kullanılır
print("Hello World \tMehmet")

# type fonksiyonu değerin hangi veri tipinde olduğunu gösterir
print(type(3.14))
print(type(3))
print(type("3"))

# sep parametresi karakterleri arasına bırakılacak değeri verir
print(35, 47, 58, 69)
print(35, 47, 58, 69, sep=":")

# Başa * karakteri koyulursa her bir karakterin arasına boşluk koyar
print(*"Python")
print(*"TBMM", sep=".")

# Formatlama
print("{} {} {} {}".format(3.14, 2.15, 25.47, 45.45))

# Süslü parantezlerin hangi sırayla alınacağı belirlenir
print("{1} {2} {0} {3}".format("test", 2, 25.47, "son"))

# Virgülden sonra kaç basamak alınacak
print("{:.2f}".format(3.4587555))

# DAHA FAZLA DETAY İÇİN https://pyformat.info/ sitesinden bakılabilir
