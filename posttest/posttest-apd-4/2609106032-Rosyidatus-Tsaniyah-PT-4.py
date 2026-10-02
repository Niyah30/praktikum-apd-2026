username = "niyah"
password = "032"

print("=== LOGIN ===")

percobaan = 0
login = False

while percobaan < 3 and not login:
    username_input = input("Masukkan username anda: ")
    password_input = input("Masukkan password anda: ")
    percobaan += 1

    if username_input == username and password_input == password:
        login = True
        print("Login Berhasil")
    elif percobaan < 3:
        print("Username atau password salah. Sisa kesempatan:", 3 - percobaan)
    else:
        print("Login Gagal. Kesempatan habis.")
        exit()

print()
print("=== INPUT DATA SISWA ===")

daftar_nama = []
daftar_kelas = []
daftar_ikut = []
daftar_nilai = []
daftar_kategori = []
kelas_unik = []

data_input = "ya"

while data_input == "ya":
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas: ")

    while True:
        ikut = input("Apakah siswa mengikuti ujian? (ya/tidak): ")
        if ikut in ["ya", "tidak"]:
            break
        print("Input tidak valid. Silakan input ulang.")

    if ikut == "tidak":
        nilai = 0
    else:
        while True:
            benar = int(input("Jumlah soal benar: "))
            salah = int(input("Jumlah soal salah: "))
            if benar + salah == 20:
                break
            print("Total jawaban harus 20. Silakan input ulang.")
        nilai = benar * 5

    if nilai >= 80:
        kategori = "Sangat baik"
    elif nilai >= 60:
        kategori = "Baik"
    elif nilai >= 40:
        kategori = "Cukup"
    else:
        kategori = "Perlu belajar lagi"

    print("Nilai", nama, ":", nilai)
    print()

    daftar_nama.append(nama)
    daftar_kelas.append(kelas)
    daftar_ikut.append(ikut)
    daftar_nilai.append(nilai)
    daftar_kategori.append(kategori)

    if kelas not in kelas_unik:
        kelas_unik.append(kelas)

    while True:
        data_input = input("Apakah masih ingin menginput data siswa? (ya/tidak): ")
        if data_input in ["ya", "tidak"]:
            break
        print("Input tidak valid. Silakan input ulang.")
    print()

print("=== NILAI SELURUH SISWA ===")
print()
for kls in kelas_unik:
    print("Kelas", kls)
    for i in range(len(daftar_nama)):
        if daftar_kelas[i] == kls:
            print("Nama        :", daftar_nama[i])
            print("Ikut ujian  :", daftar_ikut[i])
            print("Nilai       :", daftar_nilai[i])
            print("Kategori    :", daftar_kategori[i])
            print()
    print()