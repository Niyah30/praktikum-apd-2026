#kartu = {"merah", "merah", "biru", "hijau"}
#kartu.discard("kuning")
#kartu.remove("merah")

#print(kartu)

#aslab1 = {"fina", "shasha", "risma"}
#aslab2 = {"larry", "attar", "haekal"}
#gabung = aslab1.union(aslab2)
#print(gabung)

#Biodata = {
#"Nama" : "Siti Julpa",
#"NIM" : 25091060,
#"KRS" : ["Struktur Data", "Basis Data"],
#"Mahasiswa_Aktif" : True,
#"Instagram" : "julpatarr"
#}

#print(f"Nama saya adalah {Biodata.get('Nama')}")
#print(Biodata.get("Nama"))
#print(Biodata.get("Alamat"))
#print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

#game = {
#"pou" : "chill",
#"genshin impact" : "action",
#"valorant" : "fps",
#"minecraft" : "sandbox",
#"mobile legend" : "moba"
#}

#game.update({"resident evil" : "horror"})
#coba = game.pop("resident evil")
#print(game)
#print(coba)

#print(game)
#print(len(game))

#gamebaru = game.copy()
#print(game)
#print(gamebaru)

#key = "ayam geprek", "ayam goreng", "ayam bakar",
#value = 12000
#menu = dict.fromkeys(key, value)
#print(menu)

#poli_umum = {"Andi", "Budi", "Citra", "Doni"}
#poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
#gabung = poli_umum.union(poli_gigi)
#print(gabung)

data_siswa = {
    "siswa1" : {
        {"nama" : "johann",
        "kelas" : "A2",
        "nilai" : 95
        }
    },
    "siswa2" : {
        {"nama" : "niyah",
        "kelas" : "A2",
        "nilai" : 96
        }
    }
}
print(data_siswa)