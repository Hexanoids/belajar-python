
"""
angka =int(input('Masukkan angka : '))

if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")
else:
    print("Nol")


print('=============Latihan 1=============')

angka = int(input("Masukkan angka : "))

if angka % 2 == 0 :
    print('Genap')
else:
    print('Ganjil')


print('=============Latihan 2=============')

nilai = int(input("Masukkan nilai : "))

if nilai >=85 and nilai <=100:
    print("A")
elif nilai >=70 and nilai <=84:
    print("B")
elif nilai >=55 and nilai <=69:
    print("C")
elif nilai <=54:
    print("D")
else:
    print("Error")


print('=============Latihan 3=============')
angka1 = int(input("Input angka pertama: "))
angka2 = int(input("Input angka kedua: "))

print(f"Angka pertama: {angka1}")
print(f"Angka kedua: {angka2}")

print(f"{angka1} + {angka2} = {angka1 + angka2}")
print(f"{angka1} - {angka2} = {angka1 - angka2}")
print(f"{angka1} * {angka2} = {angka1 * angka2}")


if angka2 == 0:
    print("Tidak bisa dibagi 0.")
else:
    print(f"{angka1} / {angka2} = {angka1 / angka2}")
"""

print('=============Latihan 4=============')

umur = int(input("Masukkan umur : "))
ktp = input("Punya KTP (ya/tidak) : ")

if umur >= 17:
    if ktp == "ya":
        print("Boleh mendaftar")
    else:
        print("Belum memenuhi syarat ktp")
else:
    print("Belum memenuhi syarat umur")

