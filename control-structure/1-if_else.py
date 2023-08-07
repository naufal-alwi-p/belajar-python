# Python Conditions and If statements
# An "if statement" is written by using the if keyword.

angka1 = 12
angka2 = 10

if angka1 > angka2:
    print(angka1, 'lebih besar dari', angka2)

print("Selamat Pagi\n")

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
koma1 = 43.6
koma2 = 43.6

if koma1 > koma2:
    print(koma1, "lebih besar dari", koma2)
elif koma1 == koma2:
    print(koma1, "sama dengan", koma2)

print("Selamat Siang\n")

# The else keyword catches anything which isn't caught by the preceding conditions.
# else akan dijalankan jika semua kondisi if & elif tidak ada yang terpenuhi

huruf1 = "a"

if huruf1 == "A":
    print("Nilai A")
elif huruf1 == "B":
    print("Nilai B")
else:
    print("Maaf Format Tidak Sesuai")

print()

angka3 = 17

if (angka3 % 2) == 0:
    print(angka3, "adalah angka genap")
else:
    print(angka3, "adalah angka ganjil")

print()

# ----------------------------------------------------------------------------------
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
if 12 > 3: print("12 lebih besar dari 3\n")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
nilai1 = 78
print("Bagus") if nilai1 >= 75 else print("Kurang Bagus")
print()
# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line
huruf2 = "B"
print("Hebat") if huruf2 == "A" else print("Bagus") if huruf2 == "B" else print("Lumayan") if huruf2 == "C" else print("Kurang")


# Kamu bisa menggabungkan pengecekkan kondisi dengan logical operator (and, or) dan membalikkannya hasilnya (not)
list1 = [89, "One Piece", False]
list2 = [79, "Monogatari"]

if list1[0] > 85 and list2[0] < 80:
    print("Angka Memenuhi")
else:
    print("Angka Tidak Memenuhi")

print()

if list1[1] == "One Piece" or list2[1] == "Naruto":
    print("Anime")
else:
    print("Bukan Anime")

print()

if not list1[2]:
    print("Ini Benar Meskipun Salah")
else:
    print("Ini Salah Meskipun Benar")

print()

# You can have if statements inside if statements, this is called nested if statements.
list3 = [98, "Nasi Padang"]

if list3[0] > 80:
    if list3[1] == "Nasi Goreng":
        print("Nasi Goreng Enak")
    else:
        print("Ini Bukan Nasi Goreng >:(")
else:
    print("Angkanya Terlalu Kecil")

print()

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put
# in the pass statement to avoid getting an error.

if 17 == 17:
    pass
else:
    print("Tidak Sama Dengan")
print("Hai")