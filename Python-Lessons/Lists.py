# Liste tanımlama
lists = [1, "test", 5, "test2"]
print(type(lists))

# Boş liste oluşturma
list1 = []
print(list1)

emptyList = list()
print(emptyList)

# Listenin uzunluğunu öğrenme
list2 = [1, 2, 3, 6, 5]
print(len(list2))

# Stringi listeye çevirme
listChar = list("Hello")
print(listChar)

list3 = [1, 2, 3, 6, 5, 8, 7]
print(list3[2])

# sondaki elemana ulaşır
print(len(list3))

# Liste parçalama 1'den sona kadar parçalama
print(list3[1:])

# Liste parçalama 0'den 4. indekse parçalama
print(list3[:4])

# Liste parçalama aştan sona git 2şer atlayarak parçalama
print(list3[::2])

# List birleştirme
list1 = list("beşik")
list2 = list("taşlık")
list3 = list1[::] + list2[:3]
print(list3)

list4 = list1 * 3
print(list4)

# 0 dan 2 indekse kadar eleman değiştirme
list3 = [1, 2, 3, 4, 5, 6, 7]
list3[:2] = [10, 11]
print(list3)

# append metodu listeye eleman ekleme
list3 = [1, 2, 3, 4, 5, 6, 7]
list3.append(10)
print(list3)

list4 = [8, 9]
list3.append(list4)
print(list3)

# pop metodu son elemanı atma
list3 = [1, 2, 3, 4, 5, 6, 7]
list3.pop()
print(list3)

# sort metodu sıralama
list3 = [10, 2, 30, 40, 5, 60, 7]
list3.sort()
print(list3)

# tersten sıralam metodu reverse
list3.sort(reverse=True)
print(list3)

# iç içe listeler
list3 = [10, 2, [30, 40], 5, [60, 7]]
print(list3[2][0])

# liste kaç tane istenilen eleman var
print(list3.count(5))

