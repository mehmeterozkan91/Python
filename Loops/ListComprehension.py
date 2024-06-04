# List comprehension (liste atama)

lists = [(1, 2), (3, 4), (5, 6), (7, 8)]
lists2 = [i for i, j in lists]
print(lists2)
"""
Çıktı

[1, 3, 5, 7]
"""

list1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
list3 = [x for i in list1 for x in i]
print(list3)

"""
Çıktı

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""