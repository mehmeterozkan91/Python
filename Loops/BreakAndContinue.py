# Break ve Continue kullanımı

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        break #break kullanınca direk while döngüsünden çıkıyor

"""
Çıktı

0
1
2
3
4

"""

i = 0
while True:
    name = input("İsim (çıkmak için q bas): ")
    if name == "q":
        break;

"""
Çıktı

İsim (çıkmak için q bas): s
İsim (çıkmak için q bas): a
İsim (çıkmak için q bas): q
"""

for i in range(10):
    if i == 5:
        continue # continue olduğunda döngü aşağıya gitmez döngünün başına döner
    print(i)

"""
Çıktı

0
1
2
3
4
6
7
8
9
"""

