from data import barang
from fungsiBantu import input_wajib, input_angka, cek_akses, jeda
from tampilan import tampil_menu, tampil_barang
from read import cari_barang

def edit_laporan(username, role):
    print("---Edit Laporan---" if role == "admin" else "---Edit Laporan Saya---")
    daftar = cari_barang(4, "", username, role)
    if len(daftar) == 0:
        print("Belum ada laporan yang bisa diedit.")
        jeda()
        return
    tampil_barang(daftar)
    id_cari = input_wajib("Masukkan ID barang: ").upper()
    if id_cari not in barang:
        print("Data tidak ditemukan.")
    elif not cek_akses(id_cari, username, role):
        print("Anda tidak memiliki akses untuk mengedit laporan ini.")
    else:
        tampil_menu("Edit", {
            1: "Ubah nama barang",
            2: "Ubah detail barang",
            3: "Ubah lokasi",
            4: "Ubah status",
        })
        pilih = input_angka ("Pilih yang diedit: ")
        if pilih in (1, 2, 3):
            baru = input_wajib("Masukkan data baru: ")
            kolom = {
                1: "nama",
                2: "detail",
                3: "lokasi"
            }
            barang[id_cari][kolom[pilih]] = baru
            print("Laporan berhasil diubah.")
        elif pilih == 4:
            if barang[id_cari]["status"] == "Sudah kembali":
                print("Barang ini sudah kembali")
            else:
                yakin = input_wajib("Pemilik asli sudah diverifikasi? (y/n): ").lower()
                if yakin == "y":
                    barang[id_cari]["status"] = "Sudah kembali"
                    print("Status laporan berhasil diubah menjadi 'Sudah kembali'.")
                else:
                    print("Dibatalkan.")
        else:
            print("Pilihan tidak valid.")
    jeda()