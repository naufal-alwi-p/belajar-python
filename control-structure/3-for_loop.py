# Berbeda dengan mayoritas bahasa pemrograman lain, di dalam Python perulangan for lebih ke perulangan untuk memproses
# array / himpunan. Ini mirip seperti perulangan foreach di bahasa PHP.

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found
# in other object-orientated programming languages.
# The for loop does not require an indexing variable to set beforehand.

data1 = [12 + 2j, "Makan", 45210, 5.42, False, b"Tahu"]

for i in data1:
    print(i)

print()

# Even strings are iterable objects, they contain a sequence of characters
teks1 = "Selamat Pagi"

for i in teks1:
    print(i)

print()

# With the break statement we can stop the loop before it has looped through all the items
teks2 = "ABCabcDEFdef"

for i in teks2:
    if i == "b":
        break
    print(i)

print()

# With the continue statement we can stop the current iteration of the loop, and continue with the next
data2 = {"Nilai", False, 12j, 65.2, 23091, True, 12j}
print(type(data2), "\n")

for i in data2:
    if(i == False):
        continue
    print(i)

print()

# Struktur perulangan di bahasa Python sepintas tidak memungkinkan kita untuk membuat perulangan angka naik, misalnya
# dari 1, 2, 3, dst. Namun ini bisa dibuat dengan bantuan fungsi atau function range().
# Fungsi range() bisa dipakai untuk membuat deret angka, yang kemudian menjadi inputan ke dalam perulangan for.

# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and
# ends at a specified number.

for i in range(7):
    print(i)
# Note that range(7) is not the values of 0 to 7, but the values 0 to 6.
print()

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding
# a parameter: range(3, 7), which means values from 3 to 7 (but not including 7)

for i in range(3, 7):
    print(i)

print()

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by
# adding a third parameter: range(1, 30, 5)

for i in range(0, 30, 5):
    print(i)

print()

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for i in range(3):
    print(i)
else:
    print("Perulangan Selesai")

print()

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for i in range(7):
    if i == 3:
        break
    print(i)
else:
    print("Ini akan tampil jika perulangan tidak dihentikan oleh break")

print()

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in range(2):
    pass
print(":D\n")

# A nested loop is a loop inside a loop.
for i in range(3):
    for j in range(5):
        print(i, "=>", j)

# Tambahan
kamus = {"Prodi": "Ilmu Komputer", "Fakultas": "MIPA", "Umur": 20}

print("Key:")
for i in kamus:
    print(i)

print("\nValue:")
for i in kamus.values():
    print(i)

print("\nKey & Value:")
for (x, y) in kamus.items():
    print(x, ":", y)
