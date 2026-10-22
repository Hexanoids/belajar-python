USERNAME = "admin"
PASSWORD = "adminjuga"
MAX_PERCOBAAN = 3

percobaan = 0
berhasil = False

while percobaan < MAX_PERCOBAAN:
    username = input("Username : ")
    password = input("Password : ")
    percobaan += 1

    if username == USERNAME and password == PASSWORD:
        berhasil=True
        break

    sisa = MAX_PERCOBAAN - percobaan
    if sisa > 0:
        print(f"Login gagal. Sisa percobaan : {sisa}")

if berhasil:
    print("Login berhasil. Selamat datang!")
else:
    print("Akun dikunci karna terlalu banyak percobaan")


