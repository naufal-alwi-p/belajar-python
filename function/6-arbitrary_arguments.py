# Arbitrary arguments adalah istilah untuk menyebut jumlah argumen yang tidak bisa ditentukan atau berubah-ubah.
# Dengan menggunakan teknik arbitrary arguments, kita bisa membuat sebuah fungsi untuk menerima 3, 4 atau 100 argumen sekaligus.
# Nama parameter boleh bebas, selama diawali dengan tanda bintang satu ” * “.
# Dengan penulisan seperti ini, parameter *args akan menampung semua argumen yang ditulis pada saat pemanggilan fungsi tersebut
# dan disimpan dalam sebuah tuple.

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the
# function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
# Arbitrary Arguments are often shortened to *args in Python documentations.

def total(*angka):
    print("Tipe data arbitrary arguments:", type(angka))
    hasil = 0
    for i in angka:
        hasil += i
    print(hasil)

total(12, 54, 21, 5, 65)

# Jika diberi tipe data sequence yang lain (list, dictionary, set), maka akan seperti array bersarang, dalam kasus ini tuple
# berisi tipe data sequence lainnya

def tes(*data):
    print("Tes Tipe Data Argument:", type(data))
    for i in data:
        print(i, type(i))

tes([12, 65, "Nasi"])