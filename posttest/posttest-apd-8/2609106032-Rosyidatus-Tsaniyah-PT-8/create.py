from tampilan import tampil_menu
from fungsiBantu import input_angka, jeda, input_wajib
from data import counter, barang
from datetime import datetime

def buat_id():
    id_barang = "A" + str(counter["nomor"])
    counter["nomor"] += 1
    return id_barang

def input_jenis():
    while True:
        tampil_menu("Jenis Laporan", {
            1: "Hilang",
            2: "Ditemukan"
        })
        j = input_angka("Jenis Laporan: ")
        if j == 1:
            return "Hilang"
        elif j == 2:
            return "Ditemukan"
        else:
            print("Pilihan tidak valid.")

def lapor_barang(username):
    print("---Lapor Barang---")
    try:
        jenis = input_jenis()
        nama = input_wajib ("Nama Barang: ")
        detail = input_wajib ("Detail Barang: ")
        lokasi = input_wajib ("Lokasi: ")
        id_barang = buat_id()
        barang[id_barang] = {
            "nama": nama,
            "detail": detail,
            "lokasi": lokasi,
            "tanggal": datetime.now().strftime("%d-%m-%Y"),
            "jenis": jenis,
            "status": "Belum selesai",
            "pelapor": username
        }
        print(f"Laporan berhasil dibuat dengan ID: {id_barang}")
    finally:
        jeda()