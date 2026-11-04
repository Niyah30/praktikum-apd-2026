from data import barang
from fungsiBantu import jeda, input_angka, input_wajib, cek_akses
from tampilan import tampil_menu, tampil_barang

def cari_barang(pilihan, kunci, username, role):
    hasil = {}
    if pilihan == 1:
        for b in barang:
            if barang[b]["jenis"] == "Hilang" and barang[b]["status"] == "Belum selesai":
                hasil[b] = barang[b]
    elif pilihan == 2:
        for b in barang:
            if barang[b]["jenis"] == "Ditemukan" and barang[b]["status"] == "Belum selesai":
                hasil[b] = barang[b]
    elif pilihan == 3:
        for b in barang:
            if barang[b]["lokasi"].lower() == kunci.lower() and barang[b]["status"] == "Belum selesai":
                hasil[b] = barang[b]
    elif pilihan == 4:
        for b in barang:
            if cek_akses(b, username, role):
                hasil[b] = barang[b]
    return hasil

def hitung_belum_selesai(n):
    if n == 0:
        return 0
    id_barang = "A" + str(n)
    if id_barang in barang and barang[id_barang]["status"] == "Belum selesai":
        return 1 + hitung_belum_selesai(n - 1)
    else:
        return hitung_belum_selesai(n - 1)

def lihat_katalog(username, role):
    print("---Katalog Barang---")
    if len(barang) == 0:
        print("Belum ada laporan.")
    else:
        menu = {
            1: "Barang hilang",
            2: "Barang temuan",
            3: "Berdasarkan lokasi",
            4: "Semua laporan" if role == "admin" else "Laporan saya",}
        tampil_menu("Katalog", menu)
        pilih = input_angka("Pilih menu: ")
        if pilih in (1, 2, 3, 4):
            kunci = input_wajib("Masukkan lokasi: ") if pilih == 3 else ""
            hasil = cari_barang(pilih, kunci, username, role)
            if len(hasil) == 0:
                print("Tidak ada laporan yang sesuai.")
            else:
                tampil_barang(hasil)
        else:
            print("Pilihan tidak valid.")
    jeda()