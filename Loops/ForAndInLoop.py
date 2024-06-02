# For ve In Döngüleri
numbers = [1, 2, 3, 4, 5]
a = 2 in numbers
print(a)

for i in numbers:
    if i % 2 == 0:
        print("{} çift sayıdır".format(i))
    else:
        print("{} tek sayıdır".format(i))

# Demet (Tuple) for döngüsü
tuples = [(1, 2), (3, 4), (5, 6)]
for (k, v) in tuples:
    print("k:{} v:{}".format(k, v))

tuples = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
for (k, v, t) in tuples:
    print("k:{} v:{} t:{}".format(k, v, t))

tuples = [(1, 2), (3, 4, 5), (5, 6)]
for (k, v) in tuples:
    print("k:{} v:{} ".format(k, v))