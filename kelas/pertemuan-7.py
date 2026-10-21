# fungsi
# tanpa parameter
# print()
# def luas_persegi_panjang():
#    luas = 3 * 5
#    return luas

# print(luas_persegi_panjang())

# menggunakan parameter
# def luas_persegi(sisi):
#    luas = sisi * sisi
#    return luas

# print(luas_persegi(7))
# print()

# prosedur
# tanpa parameter
# def pengumuman():
#    print("Hari ini praktikum APD")

# pengumuman()

# menggunakan parameter
# def nama_pengguna(nama):
#    print(f"Nama pengguna: {nama}")

# nama_pengguna("Niyah")
# print()

# variabel
# nama = "Larry" 
# prodi = "Informatika"
# def data():
#    nama = "Teknik Kedokteran"
#    prodi = "Kedokteran Lanjut"
#    print("Nama:", nama)
#    print("Prodi:", prodi)
# data()
# print("Nama:", nama)
# print("Prodi:", prodi)

# print()

# def faktorial(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return n * faktorial(n - 1)

# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4!: {hasil_faktorial}")

# def hitung(a):
#    if a == 0:
#        print ("Selesai!")
#    else:
#        print (a)
#        hitung(a - 1)

# hitung(5)
# print(hitung)

# buku = []

# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#         for indeks in range(len(buku)):
#             print(indeks, "|", buku[indeks])

# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")

# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     menu = input("PILIH MENU > ")
#     print("\n")
#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")

# while (True):
#     tampilkan_menu()

