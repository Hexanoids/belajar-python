from datetime import date

print("Soal 1")
tahun_lahir = int(input("Berapa tahun lahirmu? "))
tahun_ini = date.today().year
print(f"Umurmu sekarang adalah {tahun_ini - tahun_lahir} tahun")

print("Soal 2")
angka1 = int(input("Input angka pertama: "))
angka2 = int(input("Input angka kedua: "))

print(f"Angka pertama: {angka1}")
print(f"Angka kedua: {angka2}")

print(f"{angka1} + {angka2} = {angka1 + angka2}")
print(f"{angka1} - {angka2} = {angka1 - angka2}")
print(f"{angka1} * {angka2} = {angka1 * angka2}")
print(f"{angka1} / {angka2} = {angka1 / angka2}")