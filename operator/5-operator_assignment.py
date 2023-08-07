# Operator assignment adalah operator untuk memasukkan suatu nilai ke dalam variabel. Operator ini sebenarnya sudah sering
# kita pakai sepanjang tutorial bahasa Python. Dalam bahasa Python, operator assignment menggunakan tanda sama dengan (=).

# Pembacaan operasi assignment dilakukan dari kanan ke kiri, bukan dari kiri ke kanan seperti yang biasa kita pahami dalam matematika.
# Operator assignment ini disebut juga sebagai operator penugasan.

# Assignment operators are used to assign values to variables
nama = 'Naufal Alwi Pratama'
angka = 154
koma = 16.5
imaginer = 1 + 5j

# Operator assignment juga memiliki variasi penulisan yang disebut sebagai operator assignment gabungan (compound assignment).
# Operator assignment gabungan adalah cara penulisan singkat operator assignment yang digabung dengan dengan operator lain.

# Operator Assignment Gabungan Aritmatika

a = 3

# a = a + 5
a += 5
print(a)

# a = a -2
a -= 2
print(a)

# a = a * 7
a *= 7
print(a)

# a = a / 2
a /= 2
print(a)

# a = a % 8
a %= 8
print(a)

# a = a // 2
a //= 2
print(a)

# a = a ** 4
a **= 4
print(a)

# --------------------------------------------------------------------------------------------
# Operator Assignment Gabungan Bitwise

x = 12

# x = x & 7
x &= 7
print(x)

# x = x | 12
x |= 12
print(x)

# x = x ^ 5
x ^= 5
print(x)

# x = x << 2
x <<= 2
print(x)

# x = x >> 3
x >>= 3
print(x)
