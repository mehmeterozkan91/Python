# Tam sayıyı ondalık sayıya çevirme
# Çevireceğimiz değişken parantez içine alınır float()
a = 7
a = float(a)
print(a)

# Ondalıklı sayıyı tam sayıya çevirme int()
b = 8.9855
b = int(b)
print(b)

# Sayıyı String'e çevirme
c = 57.78
t = str(c)
z = t + ' sayısı stringe çevrildi.'
print(z)

# String ondalıklı ve tam sayıya çevirme
s = "2.14"
t = float(s)
print(t)

#Hatalı kod
s = "2.14asas"
t = float(s)
print(t)