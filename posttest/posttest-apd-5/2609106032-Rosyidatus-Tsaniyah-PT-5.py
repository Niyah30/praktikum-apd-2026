import os

users = [["niyah", "032", "admin"]]
barang = []
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
        print("--- REGISTER ---")
        while True:
            username = input("Username: ")
            if len(username) == 0:
                print("Username tidak boleh kosong!")
                continue
            sudah_ada = False
            for u in users:
                if u[0] == username:
                    sudah_ada = True
            if sudah_ada:
                print("Username sudah dipakai!")
            else:
                break

        while True:
            password = input("Password (min. 4 karakter): ")
            if len(password) < 4:
                print("Password terlalu pendek!")
            else:
                break

        users.append([username, password, "user"])
        print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    elif menu == "2":
        print("--- LOGIN ---")
        username = input("Username: ")
        password = input("Password: ")
        login_ok = False
        for u in users:
            if u[0] == username and u[1] == password:
                login_ok = True
                role = u[2]
        if not login_ok:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut...")
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
            print("3. Edit laporan")
            print("4. Hapus laporan")
            print("5. Logout")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                print("--- LAPOR BARANG ---")
                print("1. Hilang")
                print("2. Ditemukan")
                j = input("Jenis laporan: ")
                if j == "1":
                    jenis = "Hilang"
                elif j == "2":
                    jenis = "Ditemukan"
                else:
                    print("Pilihan tidak valid")
                    input("Tekan Enter untuk lanjut...")
                    continue

                nama = input("Nama barang: ")
                detail = input("Detail barang: ")
                lokasi = input("Lokasi: ")

                if len(nama) == 0 or len(detail) == 0 or len(lokasi) == 0:
                    print("Semua data harus diisi!")
                else:
                    id_barang = "A" + str(nomor)
                    barang.append([id_barang, nama, detail, lokasi, jenis, "Belum diambil", username])
                    nomor = nomor + 1
                    print("Laporan berhasil ditambahkan dengan ID", id_barang)
                input("Tekan Enter untuk lanjut...")

            elif pilih == "2":
                print("--- KATALOG BARANG ---")
                if len(barang) == 0:
                    print("Belum ada laporan.")
                else:
                    print("1. Barang hilang")
                    print("2. Barang ditemukan")
                    print("3. Berdasarkan lokasi")
                    print("4. Laporan saya")
                    p = input("Pilih: ")
                    hasil = []
                    valid = True

                    if p == "1":
                        for b in barang:
                            if b[4] == "Hilang" and b[5] == "Belum diambil":
                                hasil.append(b)
                    elif p == "2":
                        for b in barang:
                            if b[4] == "Ditemukan" and b[5] == "Belum diambil":
                                hasil.append(b)
                    elif p == "3":
                        kunci = input("Lokasi: ").lower()
                        for b in barang:
                            if b[3].lower() == kunci and b[5] == "Belum diambil":
                                hasil.append(b)
                    elif p == "4":
                        for b in barang:
                            if b[6] == username:
                                hasil.append(b)
                    else:
                        print("Pilihan tidak valid!")
                        valid = False

                    if valid:
                        if len(hasil) == 0:
                            print("Data tidak ditemukan.")
                        else:
                            print()
                            for b in hasil:
                                print(f"ID       : {b[0]}")
                                print(f"Nama     : {b[1]}")
                                print(f"Detail   : {b[2]}")
                                print(f"Lokasi   : {b[3]}")
                                print(f"Jenis    : {b[4]}")
                                print(f"Status   : {b[5]}")
                                print(f"Pelapor  : {b[6]}")
                                print("==============================")
                input("Tekan Enter untuk lanjut...")

            elif pilih == "3":
                print("--- EDIT LAPORAN ---")
                id_cari = input("Masukkan ID barang: ").upper()
                ditemukan = False
                for i in range(len(barang)):
                    if barang[i][0] == id_cari:
                        ditemukan = True
                        if role == "admin" or barang[i][6] == username:
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
                                        barang[i][1] = baru
                                    elif e == "2":
                                        barang[i][2] = baru
                                    else:
                                        barang[i][3] = baru
                                    print("Laporan berhasil diubah.")
                            elif e == "4":
                                if barang[i][5] == "Sudah Dikembalikan":
                                    print("Barang ini sudah dikembalikan.")
                                else:
                                    yakin = input("Pemilik asli sudah diverifikasi? (y/n): ").lower()
                                    if yakin == "y":
                                        barang[i][5] = "Sudah Dikembalikan"
                                        print("Status berhasil diubah.")
                                    else:
                                        print("Dibatalkan.")
                            else:
                                print("Pilihan tidak valid!")
                        else:
                            print("Kamu hanya bisa mengedit laporan milikmu sendiri!")
                        break
                if not ditemukan:
                    print("Data tidak ditemukan.")
                input("Tekan Enter untuk lanjut...")

            elif pilih == "4":
                print("--- HAPUS LAPORAN ---")
                id_cari = input("Masukkan ID barang: ").upper()
                ditemukan = False
                for i in range(len(barang)):
                    if barang[i][0] == id_cari:
                        ditemukan = True
                        if role == "admin" or barang[i][6] == username:
                            yakin = input("Yakin hapus laporan ini? (y/n): ").lower()
                            if yakin == "y":
                                barang.pop(i)
                                print("Laporan berhasil dihapus.")
                            else:
                                print("Dibatalkan.")
                        else:
                            print("Kamu hanya bisa menghapus laporan milikmu sendiri!")
                        break
                if not ditemukan:
                    print("Data tidak ditemukan.")
                input("Tekan Enter untuk lanjut...")

            elif pilih == "5":
                break

            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")

    elif menu == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")