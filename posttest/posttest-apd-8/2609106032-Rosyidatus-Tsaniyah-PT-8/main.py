from fungsiBantu import clear_screen, jeda, input_angka
from tampilan import tampil_menu, tampil_info
from autentikasi import register, login
from data import counter
from create import lapor_barang
from read import lihat_katalog, hitung_belum_selesai
from update import edit_laporan
from delete import hapus_laporan

def menu_awal():
    while True:
        clear_screen()
        tampil_menu("Barang Hilang & Temuan di Kampus", {
            1: "Register",
            2: "Login",
            3: "Keluar"
        })
        pilih = input_angka("Pilih menu: ")

        if pilih == 1:
            register()
        elif pilih == 2:
            username, role = login()
            if username != "":
                menu_kedua(username, role)
        elif pilih == 3:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

def menu_kedua(username, role):
    while True:
        clear_screen()
        tampil_info(username, role, hitung_belum_selesai(counter['nomor']-1))
        akhiran = "" if role == "admin" else " saya"
        tampil_menu("Barang Hilang & Temuan di Kampus", {
            1: "Lapor barang",
            2: "Lihat katalog",
            3: "Edit laporan" + akhiran,
            4: "Hapus laporan" + akhiran,
            5: "Logout"
        })
        pilih = input_angka("Pilih menu: ")

        if pilih == 1:
            lapor_barang(username)
        elif pilih == 2:
            lihat_katalog(username, role)
        elif pilih == 3:
            edit_laporan(username, role)
        elif pilih == 4:
            hapus_laporan(username, role)
        elif pilih == 5:
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

if __name__ == "__main__":
    menu_awal()