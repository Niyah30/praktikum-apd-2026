import os

users = {"niyah" : {"password" : "032", "role" : "admin"}}
barang = {}
nomor = 1
role = ""

# Prosedur
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def tampil_barang(hasil):
    for b in hasil:
        print(f"ID: {b}")
        print(f"Nama: {hasil[b]['nama']}")
        print(f"Detail: {hasil[b]['detail']}")
        print(f"Lokasi: {hasil[b]['lokasi']}")
        print(f"Jenis: {hasil[b]['jenis']}")
        print(f"Status: {hasil[b]['status']}")
        print(f"Pelapor: {hasil[b]['pelapor']}")
        print("==============================")

# Fungsi tanpa parameter
def buat_id():
    global nomor
    id_barang = "A" + str(nomor)
    nomor += 1
    return id_barang

def input_jenis():
    while True:
        print("1. Hilang")
        print("2. Ditemukan")
        j = input_angka("Jenis laporan: ")
        if j == 1:
            return "Hilang"
        elif j == 2:
            return "Ditemukan"
        else:
            print("Pilihan tidak valid.")

# Fungsi dengan parameter
def cek_akses(id_barang, username, role):
    if role == "admin" or barang[id_barang]["pelapor"] == username:
        return True
    return False

def cari_barang(pilihan, kunci):
    hasil = {}
    if pilihan == 1:
        for b in barang:
            if barang[b]["jenis"] == "Hilang" and barang[b]["status"] == "Belum diambil":
                hasil[b] = barang[b]
    elif pilihan == 2:
        for b in barang:
            if barang[b]["jenis"] == "Ditemukan" and barang[b]["status"] == "Belum diambil":
                hasil[b] = barang[b]
    elif pilihan == 3:
        for b in barang:
            if barang[b]["lokasi"].lower() == kunci.lower() and barang[b]["status"] == "Belum diambil":
                hasil[b] = barang[b]
    elif pilihan == 4:
        for b in barang:
            if cek_akses(b, username, role):
                hasil[b] = barang[b]
    return hasil

# Error handling
def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus berupa angka!")

def input_wajib(pesan):
    while True:
        try:
            isi = input(pesan)
            if len(isi) == 0:
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            print(e)
        else:
            return isi

def cek_regis():
    while True:
        try:
            username = input_wajib("Username: ")
            if username in users:
                raise ValueError("Username sudah dipakai.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            password = input("Password (min. 4 karakter): ")
            if len(password) < 4:
                raise ValueError("Password terlalu pendek.")
            break
        except ValueError as e:
            print(e)
    return username, password

def lapor_barang(username):
    try:
        jenis = input_jenis()
        nama = input_wajib("Nama barang: ")
        detail = input_wajib("Detail barang: ")
        lokasi = input_wajib("Lokasi: ")
        id_barang = buat_id()
        barang[id_barang] = {
            "nama" : nama,
            "detail" : detail,
            "lokasi" : lokasi,
            "jenis" : jenis,
            "status" : "Belum diambil",
            "pelapor" : username
        }
        print("Laporan berhasil ditambahkan dengan ID", id_barang)
    finally:
        input("Tekan Enter untuk lanjut!")

# Fungsi rekursif
def hitung_belum_selesai(n):
    if n == 0:
        return 0
    else:
        id_barang = "A" + str(n)
        if id_barang in barang and barang[id_barang]["status"] == "Belum diambil":
            return 1 + hitung_belum_selesai(n - 1)
        else:
            return hitung_belum_selesai(n - 1)

# Program utama
while True:
    clear_screen()
    print("===Barang Hilang & Temuan di Kampus===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    menu = input_angka("Pilih menu: ")

    if menu == 1:
        print("---Register---")
        username, password = cek_regis()
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil, Silakan login!")
        input("Tekan Enter untuk lanjut!")

    elif menu == 2:
        print("---Login---")
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
        else:
            print("Username atau password salah.")
            input("Tekan Enter untuk lanjut!")
            continue

        while True:
            clear_screen()
            print("===Barang Hilang & Temuan di Kampus===")
            print(f"Login sebagai: {username} ({role})")
            print(f"Laporan belum selesai: {hitung_belum_selesai(nomor - 1)}")
            print("1. Lapor barang")
            print("2. Lihat katalog")
            if role == "admin":
                print("3. Edit laporan")
                print("4. Hapus laporan")
            else:
                print("3. Edit laporan saya")
                print("4. Hapus laporan saya")
            print("5. Logout")
            pilih = input_angka("Pilih menu: ")

            if pilih == 1:
                print("---Lapor barang---")
                lapor_barang(username)

            elif pilih == 2:
                print("---Katalog barang---")
                if len(barang) == 0:
                    print("Belum ada laporan.")
                else:
                    print("1. Barang hilang")
                    print("2. Barang ditemukan")
                    print("3. Berdasarkan lokasi")
                    if role == "admin":
                        print("4. Seluruh laporan")
                    else:
                        print("4. Laporan saya")
                    p = input_angka("Pilih: ")
                    valid = True

                    if p == 3:
                        kunci = input_wajib("Masukkan lokasi: ")
                        hasil = cari_barang(p, kunci)
                    elif p == 1 or p == 2 or p == 4:
                        hasil = cari_barang(p, "")
                    else:
                        print("Pilihan tidak valid.")
                        valid = False

                    if valid:
                        if len(hasil) == 0:
                            print("Data tidak ditemukan.")
                        else:
                            print()
                            tampil_barang(hasil)
                input("Tekan Enter untuk lanjut!")

            elif pilih == 3:
                if role == "admin":
                    print("---Edit laporan---")
                else:
                    print("---Edit laporan saya---")
                id_cari = input("Masukkan ID barang: ").upper()

                if id_cari in barang:
                    if cek_akses(id_cari, username, role):
                        print("1. Ubah nama barang")
                        print("2. Ubah detail barang")
                        print("3. Ubah lokasi")
                        print("4. Ubah status jadi Sudah Dikembalikan")
                        e = input_angka("Pilih yang diedit: ")

                        if e == 1 or e == 2 or e == 3:
                            baru = input_wajib("Isi baru: ")
                            if e == 1:
                                barang[id_cari]["nama"] = baru
                            elif e == 2:
                                barang[id_cari]["detail"] = baru
                            elif e == 3:
                                barang[id_cari]["lokasi"] = baru
                            print("Laporan berhasil diubah.")
                        elif e == 4:
                            if barang[id_cari]["status"] == "Sudah Dikembalikan":
                                print("Barang ini sudah dikembalikan.")
                            else:
                                yakin = input("Pemilik asli sudah diverifikasi? (y/n): ").lower()
                                if yakin == "y":
                                    barang[id_cari]["status"] = "Sudah Dikembalikan"
                                    print("Status berhasil diubah.")
                                else:
                                    print("Dibatalkan.")
                        else:
                            print("Pilihan tidak valid.")
                    else:
                        print("Kamu hanya bisa mengedit laporan milikmu sendiri.")
                else:
                    print("Data tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan!")

            elif pilih == 4:
                if role == "admin":
                    print("---Hapus laporan---")
                else:
                    print("---Hapus laporan saya---")
                id_cari = input("Masukkan ID barang: ").upper()

                if id_cari in barang:
                    if cek_akses(id_cari, username, role):
                        yakin = input("Yakin hapus laporan ini? (y/n): ").lower()
                        if yakin == "y":
                            del barang[id_cari]
                            print("Laporan berhasil dihapus.")
                        else:
                            print("Dibatalkan.")
                    else:
                        print("Kamu hanya bisa menghapus laporan milikmu sendiri.")
                else:
                    print("Data tidak ditemukan.")
                input("Tekan Enter untuk melanjutkan!")

            elif pilih == 5:
                break

            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan!")

    elif menu == 3:
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan!")