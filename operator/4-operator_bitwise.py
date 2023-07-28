# Bitwise adalah operator khusus untuk menangani operasi logika bilangan biner dalam bentuk bit.
# Bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri dari 2 jenis angka, yakni 0 dan 1. Jika nilai asal yang dipakai
# bukan bilangan biner, akan dikonversi secara otomatis menjadi bilangan biner. Misalnya 7 desimal = 0111 dalam bilangan biner.

# Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in two’s
# complement with an infinite number of sign bits.

# function bin() bisa dipakai untuk menampilkan versi biner dari sebuah angka desimal. Awalan 0b merupakan penanda bahwa ini adalah
# angka biner. Artinya, angka 0b1010 adalah 1010 dalam bilangan biner.

a = 23
b = 27

# & (And) Operator (Sets each bit to 1 if both bits are 1)
print("a =", bin(a), a)
print("b =", bin(b), b)
print("c =", bin(a & b), a & b, '(Hasil)')

print()

# | (Or) Operator (Sets each bit to 1 if one of two bits is 1)
print("a =", bin(a), a)
print('b =', bin(b), b)
print('c =', bin(a | b), a | b, "(Hasil)")

print()

# ^ (Xor) Operator (Sets each bit to 1 if only one of two bits is 1)
print("a =", bin(a), a)
print("b =", bin(b), b)
print("c =", bin(a ^ b), a ^ b, "(Hasil)")

print()

# ~ (Not) Operator (Inverts all the bits)

# Selanjutnya adalah operasi ~ atau not, yang akan membalikkan nilai bit sebuah variabel dari 0 menjadi 1, dan 1 menjadi nol.
# Namun perhitungan bit not ini sedikit membingungkan karena jika kita hanya membalikkan seluruh bit saja, hasilnya tidak
# sesuai dengan apa yang dihitung Python
# Ini berkaitan dengan cara bahasa python menyimpan angka biner (dan juga hampir semua bahasa pemrograman komputer modern).
# Angka biner di dalam bahasa python disimpan dalam format “Two’s complement”. Penjelasan tentang “Two’s complement” ini
# cukup panjang, jika tertarik bisa ke Two’s complement Wikipedia.
# Secara singkat, rumusnya adalah ~a = -a - 1, sehingga ~a = -23 - 1 = -24(desimal)
print(" a = ", bin(a), a)
print("~a =", bin(~a), ~a, "(Hasil)")

print()

# << (Zero fill left shift) Operator (Shift left by pushing zeros in from the right and let the leftmost bits fall off)
print("a      =", bin(a), a)
print("a << 2 =", bin(a << 2), a << 2, "(Hasil)")

print()

# >> (Signed right shift) Operator (Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off)
print("a      =", bin(a), a)
print("a >> 2 =", bin(a >> 2), a >> 2, "(Hasil)")