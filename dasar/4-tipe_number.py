# Tipe Data Number
# Interger
# Yang juga cukup unik di dalam bahasa Python, nilai maksimum integer (angka bulat) hanya dibatasi dengan jumlah memory.
num1 = 65346
print(type(num1), num1)

# Float
num2 = 65.765
# Untuk tipe data float, kita bisa menulisnya menggunakan notasi ilmiah
num3 = 2.95e12
print(type(num2), num2)
print(type(num3), num3)

# Complex Number
# Tipe data Complex Number adalah tipe data yang cukup unik dan jarang tersedia di bahasa pemrograman lain.
# Dalam teori matematika, complex number atau bilangan kompleks atau bilangan imajiner adalah sebutan untuk angka yang
# mengandung nilai akar kuadrat dari -1. Angka akar kuadrat dari -1 ini ditulis dalam Python dengan huruf j. Bilangan 5j
# sama artinya dengan 5√-1
num4 = 7j
num5 = 3 + 5j
print(type(num4), num4)
print(type(num5), num5)

print("")
print("")

# Type Convertion
# You can convert from one type to another with the int(), float(), and complex() methods
# Note: You cannot convert complex numbers into another number type.
i2f = float(num1)
print(type(i2f), i2f)

f2i = int(num2)
print(type(f2i), f2i)

i2c = complex(num1)
print(type(i2c), i2c)

f2c = complex(num2)
print(type(f2c), f2c)

print()

# Tambahan
# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called
# random that can be used to make random numbers
import random
print(random.randrange(231, 275))