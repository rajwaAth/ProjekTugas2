# percabangan IF dengan 1 kasus
Nama = input("Masukan nama anda : ")
if Nama == "Muhamad Rajwa Athoriq":
    print ("Hallo", Nama, "Selamat datang")
    print()

# percabangan IF dengan 2 kasus 
Bil1 = input("Masukan bilangan 1 : ")
Bil2 = input("Masukan bilangan 2 : ")
if Bil1>Bil2 :
    hasil = "Besar"
else :
    hasil = "Kecil"
print("Bilangan", Bil1, "lebih", hasil, "dari pada", Bil2)
print()

# percabangan IF dengan 3 kasus atau lebih
Nilai = int(input("Masukan nilai : "))
if Nilai >= 90 :
    print("Predikat A")
elif Nilai >= 80 :
    print("Predikat B")
elif Nilai >= 60 :
    print("Predikat C")
elif Nilai >= 40 :
    print("Predikat D")
else :
    print("Predikat E")

