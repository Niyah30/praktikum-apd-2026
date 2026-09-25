nama = "Rosyidatus Tsaniyah"
nim = 2609106032
nama_panggilan = "niyah"
nim_duaDigit= 32

nama_input = input("Masukkan nama panggilan anda: ").lower()
nim_input = int(input("Masukkan 2 digit terakhir nim anda: "))

if nama_input == nama_panggilan and nim_input == nim_duaDigit:
    print("Login Berhasil")
else:
    print("Login Gagal")
    exit()

print("Jenis BBM")
print("1. Pertalite       : Rp 10.000 /liter")
print("2. Pertamax        : Rp 12.500 /liter")
print("3. Pertamax Turbo  : Rp 15.000 /liter")

pilihan = int(input("Masukkan pilihan jenis BBM (1-3): "))

if pilihan == 1:
    harga = 10000
    jenis_bbm = "Pertalite"
elif pilihan == 2:
    harga = 12500
    jenis_bbm = "Pertamax"
elif pilihan == 3:
    harga = 15000
    jenis_bbm = "Pertamax Turbo"
else:
    print("Pilihan tidak valid")
    exit()

jumlah_liter = float(input("Masukkan jumlah liter yang ingin dibeli: "))

if jumlah_liter <= 0:
    print("Jumlah liter tidak valid")
    exit()

if jumlah_liter >= 10:
    persen_diskon = 0.10
elif jumlah_liter >= 5:
    persen_diskon = 0.05
else:
    persen_diskon = 0.0

total_harga = harga * jumlah_liter
diskon = persen_diskon * total_harga

member = input("Apakah anda member? (ya/tidak): ").lower()
if member == "ya":
    diskon_member = 0.02 * total_harga
else:
    diskon_member = 0.0

total_bayar = total_harga - diskon - diskon_member

print("==============================================")
print("Nama               |", nama)
print("NIM                |", nim)
print("Jenis BBM          |", jenis_bbm)
print("Jumlah liter       |", jumlah_liter)
print("Total harga (Rp)   |", total_harga)
print("Diskon (Rp)        |", diskon)
print("Diskon member (Rp) |", diskon_member)
print("Total bayar (Rp)   |", total_bayar)
print("==============================================")