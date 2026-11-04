from prettytable import PrettyTable

def tampil_menu (judul, pilihan):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ("No", "Menu")
    tabel.align["Menu"] = "l"
    for no in pilihan:
        tabel.add_row((no, pilihan[no]))
    print(tabel)

def tampil_barang(hasil):
    tabel = PrettyTable()
    tabel.field_names = ("ID", "Nama", "Detail", "Lokasi", "Tanggal", "Jenis", "Status", "Pelapor")
    for id_barang in hasil:
        b = hasil [id_barang]
        tabel.add_row((id_barang, b["nama"], b["detail"], b["lokasi"], b["tanggal"], b["jenis"], b["status"], b["pelapor"]))
    tabel.align = "l"
    print(tabel)

def tampil_info(username, role, jumlah):
    tabel = PrettyTable()
    tabel.title = "Info Akun"
    tabel.field_names = ("Login sebagai", "Role", "Laporan belum selesai")
    tabel.add_row((username, role, jumlah))
    print(tabel)