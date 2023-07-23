# Booleans represent one of two values: True or False.
benar = True
salah = False
print(benar)
print(salah)
print()

# Selain diinput manual, tipe data boolean lebih sering di dapat sebagai hasil dari operasi perbandingan
# When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(12 == 12)
print(100 < 20)
print('a' == "a")
print("A" < "a")
print()

# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool(12))
print(bool("Selamat Pagi"))
print(bool(12 + 7j))
print()

# Semua nilai bernilai True jika dikonversi ke boolean, kecuali yang dibawah ini
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print()

# Tambahan: One more value, or object in this case, evaluates to False, and that is if you have an object that
# is made from a class with a __len__ function that returns 0 or False
# Mungkin akan paham penjelasan diatas jika sudah mempelajari Python OOP

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which
# can be used to determine if an object is of a certain data type
print(isinstance("Halo", str))