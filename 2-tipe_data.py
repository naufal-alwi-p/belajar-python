# You can get the data type of any object by using the type() function
nama = "Naufal Alwi Pratama"
tipe = type(nama)

print(nama)
print("Tipe data:", tipe)

# In Python, the data type is set when you assign a value to a variable
# String
teks = "Selamat Pagi"
print(type(teks), teks)

# int (Interger)
num1 = 12
print(type(num1), num1)

# Float
num2 = 37.5
print(type(num2), num2)

# Complex Number
num3 = 7j
print(type(num3), num3)

# List
list1 = ['Nasi', "Tempe", "Kopi"]
print(type(list1), list1)

# Tuple
tuple1 = ('MTK', "Fisika", "B. Indonesia")
print(type(tuple1), tuple1)

# Range
rentang = range(7)
print(type(rentang), rentang)

# Dictionary
kamus = {"Nama": "Naufal Alwi Pratama", "Umur": 19, "NPM": "065122986"}
print(type(kamus), kamus)

# Set
set1 = {"Beli", "Olah", "Santap"}
print(type(set1), set1)

# Frozen Set
setBeku = frozenset({"Bangun", "Mandi", "Sarapan"})
print(type(setBeku), setBeku)

# Boolean
check = True
print(type(check), check)

# Bytes
biner = b"Tes"
print(type(biner), biner)

# bytearray
binerArr = bytearray(9)
print(type(binerArr), binerArr)

# memoryview
lihatMemori = memoryview(bytes(5))
print(type(lihatMemori), lihatMemori)

# None
kosong = None
print(type(kosong), kosong)