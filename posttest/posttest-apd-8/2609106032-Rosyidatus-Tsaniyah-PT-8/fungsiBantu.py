import os
import pwinput
from data import barang

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def jeda(pesan = "Tekan Enter untuk melanjutkan..."):
    input(pesan)

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus berupa angka!")

def input_wajib(pesan):
    while True:
        teks = input(pesan).strip()
        if len(teks) == 0:
            print("Input tidak boleh kosong!")
        else:
            return teks

def input_password(pesan):
    return pwinput.pwinput(pesan, mask = "*")

def cek_akses(id_barang, username, role):
    if role == "admin" or barang[id_barang]["pelapor"] == username:
        return True
    return False