import os

users = {"niyah" : {"password" : "032", "role" : "admin"}}
barang = {}
nomor = 1
role = ""

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("===Barang Hilang & Temuan di Kampus===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        print("---Register---")
        while True:
            username = input("Username: ")
            if len(username) == 0:
                print("Username tidak boleh kosong!")
            elif username in users:
                print("Username sudah dipakai.")
            else:
                break

        while True:
            password = input("Password (min. 4 karakter): ")
            if len(password) < 4 :
                print("Password terlalu pendek.")
            else:
                break

        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil, Silakan login!")
        input("Tekan Enter untuk lanjut!")

    elif menu == "2":
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
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("===Barang Hilang & Temuan di Kampus===")
            print(f"Login sebagai: {username} ({role})")
            print("1. Lapor barang")
            print("2. Lihat katalog")
            if role == "admin":
                print("3. Edit laporan")
                print("4. Hapus laporan")
            else:
                print("3. Edit laporan saya")
                print("4. Hapus laporan saya")
            print("5. Logout")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                print("---Lapor barang---")
                print("1. Hilang")
                print("2. Ditemukan")
                j = input("Jenis laporan: ")
                if j == "1":
                    jenis = "Hilang"
                elif j == "2":
                    jenis = "Ditemukan"
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk lanjut!")
                    continue

                nama = input("Nama barang: ")
                detail = input("Detail barang: ")
                lokasi = input("Lokasi: ")

                if len(nama) == 0 or len(detail) == 0 or len(lokasi) == 0:
                    print("Semua data harus diisi!")
                else:
                    id_barang = "A" + str(nomor)
                    barang[id_barang] = {
                        "nama" : nama,
                        "detail" : detail,
                        "lokasi" : lokasi,
                        "jenis" : jenis,
                        "status" : "Belum diambil",
                        "pelapor" : username
                    }
                    nomor = nomor + 1
                    print("Laporan berhasil ditambahkan dengan ID", id_barang)
                input("Tekan Enter untuk lanjut!")

            elif pilih == "2":
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
                    p = input("Pilih: ")
                    hasil = {}
                    valid = True

                    if p == "1":
                        for b in barang:
                            if barang[b]["jenis"] == "Hilang" and barang[b]["status"] == "Belum diambil":
                                hasil[b] = barang[b]

                    elif p == "2":
                        for b in barang:
                            if barang[b]["jenis"] == "Ditemukan" and barang[b]["status"] == "Belum diambil":
                                hasil[b] = barang[b]

                    elif p == "3":
                        kunci = input("Lokasi: ").lower()
                        for b in barang:
                            if barang[b]["lokasi"].lower() == kunci and barang[b]["status"] == "Belum diambil":
                                hasil[b] = barang[b]

                    elif p == "4":
                        for b in barang:
                            if role == "admin" or barang[b]["pelapor"] == username:
                                hasil[b] = barang[b]

                    else:
                        print("Pilihan tidak valid.")
                        valid = False

                    if valid:
                        if len(hasil) == 0:
                            print("Data tidak ditemukan.")
                        else:
                            print()
                            for b in hasil:
                                print(f"ID: {b}")
                                print(f"Nama: {hasil[b]['nama']}")
                                print(f"Detail: {hasil[b]['detail']}")
                                print(f"Lokasi: {hasil[b]['lokasi']}")
                                print(f"Jenis: {hasil[b]['jenis']}")
                                print(f"Status: {hasil[b]['status']}")
                                print(f"Pelapor: {hasil[b]['pelapor']}")
                                print("==============================")
                input("Tekan Enter untuk lanjut!")

            elif pilih == "3":
                if role == "admin":
                    print("---Edit laporan---")
                else:
                    print("---Edit laporan saya---")
                id_cari = input("Masukkan ID barang: ").upper()

                if id_cari in barang:
                    if role == "admin" or barang[id_cari]["pelapor"] == username:
                        print("1. Ubah nama barang")
                        print("2. Ubah detail barang")
                        print("3. Ubah lokasi")
                        print("4. Ubah status jadi Sudah Dikembalikan")
                        e = input("Pilih yang diedit: ")

                        if e == "1" or e == "2" or e == "3":
                            baru = input("Isi baru: ")
                            if len(baru) == 0:
                                print("Data tidak boleh kosong!")
                            else:
                                if e == "1":
                                    barang[id_cari]["nama"] = baru
                                elif e == "2":
                                    barang[id_cari]["detail"] = baru
                                elif e == "3":
                                    barang[id_cari]["lokasi"] = baru
                                print("Laporan berhasil diubah.")
                        elif e == "4":
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

            elif pilih == "4":
                if role == "admin":
                    print("---Hapus laporan---")
                else:
                    print("---Hapus laporan saya---")
                id_cari = input("Masukkan ID barang: ").upper()

                if id_cari in barang:
                    if role == "admin" or barang[id_cari]["pelapor"] == username:
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

            elif pilih == "5":
                break

            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan!")

    elif menu == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan!")