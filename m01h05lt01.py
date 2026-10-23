"""
print("========= Materi List =========")

buah = ["apel", "jeruk", "mangga"]
print(buah[0])
print(buah[2])
print(buah[-1])

buah.append("pisang")
buah.remove("jeruk")
print(buah)

for item in buah:
    print(item)

nilai = [80, 75, 90]
total = 0
for n in nilai:
    total += n
print(total / len(nilai))

tugas = []
tugas.append(input("Tugas : "))
print(tugas)

print("========= Latihan 1 =========")

nama = ["ayu","eko","ade","rio","gio","tia"]
for item in nama:
    print(item)
    
print(f"Total nama : {len(nama)}")

print("========= Latihan 2 =========")

nilai = [80,70,90,60,100]
total = 0
for n in nilai:
    total += n
print(f"Total nilai : {total}")
print(f"Rata-rata : {total / len(nilai)}")

"""
print("========= Latihan 3 =========")
antrian = []

while True:
    tugas = input("Tugas : ")
    if tugas == "selesai":
        break
    else:
        antrian.append(tugas)
for i in range(len(antrian)):
    print(f"{i + 1}. {antrian[i]}")