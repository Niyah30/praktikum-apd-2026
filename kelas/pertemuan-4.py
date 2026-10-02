#batas = 5
#for i in range(10): #range(start, stop, step)
#    print("Perulangan ke-", i)

#nilai = [75, 60, 80, 60, 50]
#for item in nilai:
#    if item > 70:
#        print(item, "Lulus")
#    else:
#        print(item, "Tidak Lulus")

#for i in range(0, 11, 2):
#    print(i)

#for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#        print(f'{i} x {j} = {i * j}')
#    print('') #biar ada jarak tiap iterasi

#jawab = "ya"
#hitung = 0

#while(jawab == "ya"):
#    hitung += 1
#    jawab = input("Ulang lagi tidak? ")

#print(f"Total Perulangan : {hitung}")

#for i in range(10):
#    if i == 5:
#        break
#    print(i)

#for i in range(10):
#    if i % 2 == 0:
#        continue
#    print(i)

#for i in range(10):
#    if i == 0:
#        continue
#    elif i == 5:
#        break
#    else:
#        print(i)

#for i in range(5):
#    print(i, end=" ")

#bilangan = int(input("Masukkan bilangan: "))
#jumlah_ganjil = 0
#for i in range(1, bilangan + 1):
#    if i % 2 == 1:
#        jumlah_ganjil += 1
#        print(i)
#print (f"Jumlah bilangan ganjil: {jumlah_ganjil}")

bilangan = int(input("Masukkan bilangan: "))
jumlah_ganjil = 0

while (bilangan % 2 == 1):
    jumlah_ganjil += 1
