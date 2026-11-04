from data import barang
from fungsiBantu import jeda, input_wajib, cek_akses
from tampilan import tampil_barang
from read import cari_barang

def hapus_laporan(username, role):
    print("---Hapus Laporan---" if role == "admin" else "---Hapus Laporan Saya---")
    daftar = cari_barang(4, "", username, role)
    if len(daftar) == 0:
        print("Belum ada laporan yang bisa dihapus.")
        jeda()
        return
    tampil_barang(daftar)
    id_cari = input_wajib("Masukkan ID barang: ").upper()
    if id_cari not in barang:
        print("Data tidak ditemukan.")
    elif not cek_akses(id_cari, username, role):
        print("Anda tidak memiliki akses untuk menghapus laporan ini.")
    else:
        yakin = input_wajib("Yakin hapus laporan ini? (y/n): ").lower()
        if yakin == "y":
            del barang[id_cari]
            print("Laporan berhasil dihapus.")
        else:
            print("Dibatalkan.")
    jeda()