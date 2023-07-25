# Tipe data Tuple sangat mirip seperti tipe data List yang sudah kita pelajari sebelumnya, dimana tipe data Tuple juga terdiri dari
# kumpulan tipe data lain. Bedanya, anggota di dalam tipe data Tuple tidak bisa diubah setelah di deklarasikan. Kita akan bahas
# perbedaan ini menggunakan contoh kode program.

# Untuk membuat tipe data Tuple, gunakan tanda kurung biasa, kemudian setiap anggota list dipisah dengan tanda koma
makanan = ("Nasi Goreng", "Pecel Lele", "Martabak", "Gorengan", "Kebab")
angka = (12, 65, 32.5, 12j)
data = ("Gratis", 659, 12.5, 76j, True, False)

print(type(makanan), makanan)
print(type(angka), angka)
print(type(data), data)
print()

# Cara mengakses tipe data Tuple tidak berbeda dengan tipe data List, dimana kita menulis nomor urut index dalam tanda kurung siku
print(makanan[1])
print(angka[2])
print(data[0])
print(makanan[1:4])
print(makanan[:])
print(angka[1:])
print(data[:5])

# Mencoba mengubah isi di dalam tuple
# makanan[2] = "Mie Ayam" (Error)