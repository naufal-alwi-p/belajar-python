# Tipe data dictionary adalah tipe data array dimana key atau index dari array bisa berbentuk string, tidak hanya
# number saja. Dalam bahasa pemrograman lain (seperti PHP) dictionary ini dikenal juga dengan sebutan associative array.
# Berikut format dasar penulisan dictionary dalam bahasa Python:
# nama_variabel = { "key1": "value1", "key2": "value2", "key3": "value3" }

# Dalam pembuatan dictionary, kita menggunakan tanda kurung kurawal { dan } . Selain itu setiap element merupakan pasangan
# dari key dan value. Antar satu element dengan element lain dipisah dengan tanda koma seperti contoh berikut:
makanan = {1: "Rawon", 2: "Kerak Telor", 3: "Bakso", 4:"Nasi Kuning", 5: "Batagor"}
angka = {"tinggi": 171.2, "umur": 19}
data = {"status": True, 1: "Nasi", 3: "Udang", "Alamat": "Jakarta"}
print(type(makanan), makanan)
print(type(angka), angka)
print(type(data), data)
print()

# Nilai atau value dari setiap element dictionary bisa terdiri dari berbagai tipe data
nilai = {
    "data": [12, 43, 37, 12.5],
    1: "Nilai",
    2: 2j,
    "lihat": ("Nilai", True, 120)
}
print(nilai)
print()

# Untuk menampilkan satu element yang ada di dalam dictionary, tulis key atau index yang ingin diakses dalam kurung siku
print(makanan[2])
print(angka['umur'])
print(data['Alamat'])
print()

# Kita bisa mengubah nilai dari sebuah element dictionary. Caranya mirip seperti tipe data list, yakni mengisi nilai
# ke dalam key atau index dictionary yang sudah ada
angka['tinggi'] = 172.5
print(angka)
print()

# Untuk menambah element baru ke dalam dictionary, bisa dilakukan dengan cara mengisi nilai ke sebuah key baru
angka['hobi'] = "Belajar"
print(angka)

# Untuk menghapus element dari sebuah dictionary, bisa menggunakan perintah del
del angka['hobi']
print(angka)

# Selain menggunakan tanda kurung kurawal, proses pembuatan dictionary di dalam bahasa Python juga bisa dilakukan
# menggunakan “constructor” dict()
# Dengan menggunakan perintah dict(), kita tidak lagi memakai tanda kurung kurawal, tapi cukup tanda kurung biasa.
# Selain itu key element juga tidak perlu menggunakan tanda kutip, dan tanda sama dengan ‘=’  dipakai untuk
# menginput nilai ke dalam element dictionary.
info = dict(
    # 15 = "Lima Belas", (Error) (Semoga nanti bisa mendapat penjelasannya)
    kegiatan = "Belajar",
    kursi= "Gaming",
)
print(info)