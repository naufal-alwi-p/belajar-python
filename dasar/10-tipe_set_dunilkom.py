# Tipe data Set Python adalah tipe data yang berisi kumpulan tipe data dan dipakai untuk mengolah himpunan (set).
# Jika dibandingkan dengan tipe data berbentuk array lain di Python, tipe data set berbeda dalam hal
# index, pengurutan dan keunikan nilai (unique value).

# Tipe data set tidak memiliki index, sehingga tidak ada mekanisme pengurutan. Maksudnya, ketika kita menginput beberapa
# nilai ke dalam tipe data set, posisi nilai tersebut bisa berada di mana saja, tidak persis seperti apa yang tertulis.
# Akibat tidak memiliki index, maka kita tidak bisa menambah nilai baru ke dalam tipe data set dengan cara menulis
# nomor index (seperti di dalam tipe data list)

# Ciri khas selanjutnya dari tipe data set adalah tidak bisa menerima nilai ganda, setiap nilai di dalam set harus unik.
# Jika kita menginput beberapa nilai yang sama, hanya satu yang tersimpan di dalam set.

# Untuk membuat tipe data set, gunakan tanda kurung kurawal, kemudian setiap anggota set dipisah dengan tanda koma
makanan = {"Burger", "Chicken", "Kebab", "Kornet", "Rendang"}
angka = {21, 45.154, 12 + 5j}
data = {True, "Pagi", 10021, 54.61, False, 5j, "Pagi", 21, 45.154} # Ada dua nilai "Pagi" tapi nanti hanya 1 saja yang diambil

print(type(makanan), makanan)
print(type(angka), angka)
print(type(data), data)
print("Perhatikan urutan data yang tampil, hampir semuanya tidak terurut sesuai penulisan di dalam program")
print()

# Bagaimana jika kita tetap mengakses anggota set menggunakan index ?
# print(makanan[1]) (Error)

# Operasi Himpunan tipe data Set Python
# Tipe data set pada dasarnya adalah tipe data khusus yang dipakai untuk operasi himpunan, seperti operasi gabungan
# (union), operasi irisan (intersection), dst. Lebih rinci tentang operasi himpunan ini akan kita bahas dalam
# tutorial khusus tentang operator di dalam bahasa Python.
print(angka | data) # Union
# Union adalah operasi gabungan himpunan. Hasilnya, seluruh anggota himpunan yang ada di variabel angka digabung dengan seluruh anggota
# dalam variabel data, anggota yang ada di kedua himpunan hanya akan ditampilkan 1 kali.

print(angka & data) # Intersection
# Intersection adalah operasi irisan himpunan. Hasilnya adalah seluruh anggota yang terdapat di variabel angka dan juga ada di variabel data
# (harus ada di kedua variabel).