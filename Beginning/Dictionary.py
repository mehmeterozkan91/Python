# Dictionary oluşturma

dic = {"name": "Mehmet", "age": 5, "surname": "ERÖZKAN"}
print(dic)
print(type(dic))
# dictionary eleman ekleme
dic["lang"] = "Turkish"
print(dic)

# elaman bulma
print(dic["name"])

# değer değiştirme
dic["name"] = "Mehmet ERÖZKAN"
print(dic)

dic1 = {
    "lang": {"english": "Turkish", "turkish": "Turkish"},
    "meyveler": {"kiraz": "yaz", "portakal": "kış"},
    "dates": {"90s": [1990, 1991, 1992, 1993, 1994]}
}
print(dic1["dates"]["90s"][0])

# keys değerlerini alma
print(dic1.keys())

# values değerlerini alma
print(dic1.values())

# items
print(dic1.items())

for k, v in dic1.items():
    print(k, v)
