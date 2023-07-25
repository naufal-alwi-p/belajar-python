# sebenarnya tipe data array di Python terdiri dari 4 jenis, yakni List, Tuple, Set dan Dictionary. Ke empat tipe data
# ini mirip satu sama lain dengan sedikit perbedaan. Kita akan bahas secara rinci dalam tutorial terpisah, yang dimulai
# dari List terlebih dahulu.

# Secara sederhana, tipe data List adalah sebuah array, yakni tipe data yang berisi kumpulan tipe data lain. Namun
# berbeda seperti array dalam bahasa pemrograman lain, List bisa diisi dengan berbagai jenis data, tidak harus tipe data yang sama.
# Untuk membuat tipe data List, gunakan tanda kurung siku, tiap data dipisah dengan tanda koma
makanan = ["Nasi", "Rawon", "Ketoprak", "Ikan Mas", "Gado-Gado"]
angka = [142, 54.7, 5 + 9j, 1965]
data = [128, "Pagi", True, 65.3, False, 12j]

print(type(makanan), makanan)
print(type(angka), angka)
print(type(data), data)
print()

# Untuk mengakses nilai individu dari tipe data list, gunakan penomoran index. Data pertama bernomor index 0, data kedua bernomor
# index 1, dst. Nomor index ini ditulis di dalam tanda kurung siku
print(makanan[0] + ", " + makanan[1])
print(angka[3])
print(data[2])
print()

# Nilai yang ada di dalam List bisa diganti atau diupdate. Caranya, isikan data baru ke dalam nomor index yang ingin diganti isinya
makanan[3] = "Ayam Bakar"
angka[3] = 5293
data[5] = 100 + 21j
print(makanan)
print(angka)
print(data)
print()

# Menampilkan Sebagian Anggota List
print(makanan[1:4])
print(makanan[:]) # Menampilkan Semua Isi
print(angka[1:])
print(data[:5])