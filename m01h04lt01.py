
"""
print("------------Latihan 1------------")
for i in range (1, 11):
    print(i)


print("------------Latihan 2------------")
angka = int(input("Masukkan angka : "))
for i in range (1,11):
    print(f"{angka} x {i} = {angka * i}")

print("------------Latihan 3------------")
n = int(input("Masukkan n : "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Jumlah 1 sampai {n} = {total}")

print("------------Latihan 4------------")
print("------------Cara A------------")

for i in range (2,21,2):
    print(i)
"""

print("------------Latihan 4------------")
print("------------Cara B------------")

for i in range (1,21):
    if i % 2 == 0:
        print(i) 