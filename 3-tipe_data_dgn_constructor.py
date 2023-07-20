# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions

# String
teks = str("Selamat Pagi")
print(type(teks), teks)

# int (Interger)
num1 = int(12)
print(type(num1), num1)

# Float
num2 = float(37.5)
print(type(num2), num2)

# Complex Number
num3 = complex(7j)
print(type(num3), num3)

# List
list1 = list(('Nasi', "Tempe", "Kopi"))
print(type(list1), list1)

# Tuple
tuple1 = tuple(('MTK', "Fisika", "B. Indonesia"))
print(type(tuple1), tuple1)

# Range
rentang = range(7)
print(type(rentang), rentang)

# Dictionary
kamus = dict(Nama= "Naufal Alwi Pratama", Umur= 19, NPM= "065122986")
print(type(kamus), kamus)

# Set
set1 = set(("Beli", "Olah", "Santap"))
print(type(set1), set1)

# Frozen Set
setBeku = frozenset(("Bangun", "Mandi", "Sarapan"))
print(type(setBeku), setBeku)

# Boolean
check = bool(10)
print(type(check), check)

# Bytes
biner = bytes(7)
print(type(biner), biner)

# bytearray
binerArr = bytearray(9)
print(type(binerArr), binerArr)

# memoryview
lihatMemori = memoryview(bytes(5))
print(type(lihatMemori), lihatMemori)