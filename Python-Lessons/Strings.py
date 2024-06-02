name = 'Mehmet'
print(name)

surname = "ERÖZKAN"
print(surname)

departman = """Software"""
print(departman)

# \ işareti bir sonraki gelecek karakteri karakter olarak algılama demek
city = 'Mehmet\'in memleketi İstanbul'
print(city)

# String index'leme 0=R 1=e 2=a 3=l  bu şekilde tersten indexleme -4=R -3=e -2=a -1=l
team = 'Real'
print(team[0])
print(team[-3])
print(team[2])
print(team[-1])

# String parçalama [başlama indeksi(verilmezse 0 olur) : bitiş indeksi(Dahil değil, verilmezse sonuna kadar gider) : atlama değeri]
a = ("Yazılım Mühendisliği")
print(a[1:6])
print(a[1:6:2])  # ikişer ikişer atla demek
print(a[::-1])  # String tersten yazma
print(a[:2])  # 0'dan başla 2. karaktere kadar
print(a[:-1])  # 0'dan başla son karaktere kadar

print(len(a))  # String uzunluğunu bulma

s = "Python "
t = "Proglama "
r = "Dili"
print(s + t + r)

# String değişken değiştirilmez, başka değişkene atanarak yok edilir örnek
s = s + "Java Programlama"
print(s)
