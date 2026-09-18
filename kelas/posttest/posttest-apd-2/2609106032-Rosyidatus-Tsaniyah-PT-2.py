bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10
bagasi_list = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

total_berat_akhir = (bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6)
total_berat_akhir_gram = total_berat_akhir * 1000
biaya_kompensasi = total_berat_akhir * 0.05
rata_rata = total_berat_akhir / len(bagasi_list)
bagasi_tengah = bagasi_list[2:5]

nim = 26
boolean = nim < rata_rata

print("==========DATA BAGASI PENUMPANG==========")
print("Bagasi 1 :", bagasi_1, "kg")
print("Bagasi 2 :", bagasi_2, "kg")
print("Bagasi 3 :", bagasi_3, "kg")
print("Bagasi 4 :", bagasi_4, "kg")
print("Bagasi 5 :", bagasi_5, "kg")
print("Bagasi 6 :", bagasi_6, "kg")
print("=============HASIL KALKULASI=============")
print("Total Berat Bagasi (kg) :", total_berat_akhir, "kg")
print("Total Berat Bagasi (gram) :", total_berat_akhir_gram, "gram")
print("Biaya Kompensasi Bahan Bakar :", biaya_kompensasi)
print("Rata-Rata Berat Bagasi :", rata_rata, "kg")
print("Bagasi Tengah :", bagasi_tengah)
print()
print("NIM :", nim)
print("Apakah NIM lebih kecil dari rata-rata total berat bagasi (kg)? :", boolean)
print("=========================================")