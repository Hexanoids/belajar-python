from datetime import date
"""
print("=========Latihan 01=========")
nama = input("Siapa namamu? ")
kota = input("Dari mana kamu? ")
hobi = input("Apa hobi kamu? ")
print(f"Nama : {nama}")
print(f"Kota : {kota}")
print(f"Hobi : {hobi}")

print("=========Latihan 02=========")
Panjang = float(input("Input Panjang = "))
Lebar = float(input("Input Lebar = "))

print(f"Panjang : {Panjang}")
print(f"Lebar : {Lebar}")
print(f"Luas : {Panjang * Lebar:.1f}")
print(f"Keliling : {2*(Panjang+Lebar)}")

print("=========Latihan 03=========")
suhu = float(input("Suhu Celcius : "))
fahrenheit = suhu * 9 / 5 + 32 
print(f"{suhu} C = {fahrenheit:.2f} F")

print("=========Latihan 04=========")
harga_satuan = int(input("Input harga satuan :"))
jumlah = int(input("Input jumlah : "))
total = harga_satuan * jumlah
total_ppn = total * 1.11

print(f"Harga Satuan : {harga_satuan}")
print(f"Jumlah : {jumlah}")
print(f"Total : {total}")
print(f"Total + PPN : {total_ppn:.0f}")

print("=========Latihan 05=========")

input_detik = int(input("Input detik :"))
jam = input_detik // 3600
sisa_detik = input_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"Total detik : {input_detik}")
print(f"{jam} jam {menit} menit {detik} detik")

print("=========Latihan 06=========")
total_tagihan = int(input("Total tagihan : "))
Jumlah_orang = int(input("Jumlah orang : "))

per_orang = total_tagihan // Jumlah_orang
sisa = total_tagihan % Jumlah_orang

print(f"Per orang : {per_orang}")
print(f"Sisa : {sisa}")


rint("=========Latihan 07=========")
tahun_lahir = int(input("Tahun Lahir : "))
tahun_ini = date.today().year

print(f"Umurmu sekarang : {tahun_ini - tahun_lahir}")
print(f"Kamu berumur 50 tahun pada tahun {tahun_lahir + 50}")
"""

print("=========Latihan 08=========")
a = int(input("Masukkan Bilangan A : "))
b = int(input("Masukkan Bilangan B : "))

rata2 = (a + b) / 2
pangkat = a ** b

print(f"Hasil Rata-rata : {rata2}")
print(f"Hasil Pangkat : {pangkat}")
print(f"Hasil Jumlah : {a + b}")
print(f"Hasil Selisih : {a - b}")