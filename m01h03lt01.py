"""
print("================ Materi ================")
for i in range(1, 8, 2):
    print("Halo ",i)
for i in range(1, 8, ):
    print("Hei ",i)

hitung = 1
while hitung <= 3:
    print("Hitungan ke", hitung)
    hitung = hitung + 1    

total = 0
for angka in range (1,6):
    total = total + angka
print(total)

for i in range (1, 100):
    if i == 3:
        break
    print (i)

for i in range (1, 10):
    if i == 5:
        continue
    print (i)

while True:
    kata = input ("Ketik ' keluar' untuk berhenti: ")
    if kata == "keluar":
        break
    print("Kamu mengetik: ", kata)


USERNAME = "kevin"
PASSWORD = "adaaja"
MAX_PERCOBAAN = 3
percobaan = 0
while percobaan < MAX_PERCOBAAN:
    username = input("Username : ")
    password = input("Password : ")
    percobaan += 1
    if username == USERNAME and password == PASSWORD:
        print("Berhasil")
        break
    sisa = MAX_PERCOBAAN - percobaan
    if sisa > 0 :
        print(f"Gagal, sisa percobaan {sisa}")
else:
    print(f"Percobaan login {MAX_PERCOBAAN}x gagal, akun terkunci")

    
print("================ Latihan 1 ================")

USERNAME = "kevin"
PASSWORD = "adaaja"
MAX_PERCOBAAN = 5
percobaan = 0
while percobaan < MAX_PERCOBAAN:
    username = input("Username : ")
    password = input("Password : ")
    percobaan += 1
    if username == USERNAME and password == PASSWORD:
        print("Berhasil")
        break
    
    if percobaan < MAX_PERCOBAAN :
        print(f"Gagal, percobaan ke-{percobaan} dari {MAX_PERCOBAAN}")
        
else:
    print(f"Percobaan login {MAX_PERCOBAAN}x gagal, akun terkunci")


print("================ Latihan 2 ================")

while True:
    nama = input("Masukkan nama: ").strip()
    panjangnama = len(nama)
    if panjangnama < 3:
        print("Nama terlalu pendek")
        
    else:
        break
print(f"Halo, {nama}")


print("================ Latihan 3 ================")

rahasia = 7
percobaan = 0

while True:
    tebakan = int(input("Tebak angka (1-10) : "))
    percobaan += 1
    if tebakan < rahasia :
        print("Terlalu kecil, tebak lagi")
    elif tebakan > rahasia :
        print("Terlalu besar, tebak lagi")
    else:
        print(f"Benar, angka rahasia adalah {rahasia} dan kamu menebak dalam {percobaan} percobaan")
        break
"""

print("================ Latihan 4 ================")

saldo = 0

while True:
    print("1. Lihat Saldo")
    print("2. Setor")
    print("3. Keluar")
    pilihan = (input("Pilihan : "))

    if pilihan == "1":
        print(f"Saldo anda sebesar {saldo}")
    elif pilihan == "2":
        setor = input("Masukkan Jumlah Setoran Rp.  ")
        if setor.isdigit():
            nilaisetor = int(setor)
            saldo += nilaisetor
            print("Setoran berhasil")
        else:
            print("Harap masukkan angka saja")
    elif pilihan == "3":
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valid, ulangi lagi")
