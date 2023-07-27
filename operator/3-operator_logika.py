# Operator logika adalah operator yang digunakan untuk membuat kesimpulan logis dari 2 kondisi boolean: true atau false.
# Pada prakteknya, operator logika ini banyak dipakai untuk menggabungkan beberapa hasil operasi perbandingan
# Operasi seperti ini, akan diproses dari kiri ke kanan, kecuali ditemukan tanda kurung maka itulah yang akan diproses terlebih dahulu

# Logical operators are used to combine conditional statements

# and Operator (True jika kedua kondisi True)
print("True and True :", True and True)
print("True and False :", True and False)
print("False and True :", False and True)
print("False and False :", False and False)

print()

# or Operator (True jika salah satu kondisi True)
print("True or True :", True or True)
print("True or False :", True or False)
print("False or True :", False or True)
print("False or False :", False or False)

print()

# not Operator (True jika kondsi False, dan sebaliknya)
print("not True :", not True)
print("not False :", not False)

# Sama seperti operasi perbandingan, operasi logika ini banyak dipakai pada percabangan kode program