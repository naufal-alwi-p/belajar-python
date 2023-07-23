# String menggunakan 1 tanda petik (')
teks1 = 'Halo'

# String menggunakan tanda petik dua (")
teks2 = "Selamat Pagi"

# String menggunakan tanda petik 3 kali (''') / (""")
teks3 = '''
Halo, Selamat pagi semuanya
Apa Kabar ?
'''

print(teks1)
print(teks2)
print(teks3)

# String Concatination (Penggabungan String menggunakan +)
teks4 = teks1 + ', ' + teks2

print(teks4)

# String dapat diakses seperti array
print(teks1[1])
print(teks2[1:9] + "\n")

# Karena string dapat diakses seperti array, string juga bisa diakses dengan perulangan
for x in teks1:
    print(x)

print()

# function len() Mengembalikan panjang string
print(str(len(teks2)) + "\n")

# To check if a certain phrase or character is present in a string, we can use the keyword in.
print('Pagi' in teks2)
print()

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("Tahu" not in teks3)
print()

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Note: The first character has index 0.
print(teks2[2:10])
print()

# By leaving out the start index, the range will start at the first character:
print(teks2[:5])
print()

# By leaving out the end index, the range will go to the end:
print(teks2[1:])
print()

# Use negative indexes to start the slice from the end of the string:
print(teks2[-7:-3])
print()

# Modify Strings
# Python has a set of built-in methods that you can use on strings.
# Upper Case (upper() method)
print(teks2.upper())
print()

# Lower Case (lower() method)
print(teks1.lower())
print()

# Remove Whitespace (strip() method)
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
teks5 = "                         Nasi Goreng Sedaap                 "
print(teks5)
print(teks5.strip())
print()

# Replace String (replace() method)
# The replace() method replaces a string with another string:
teks6 = "Lontong Sayur"
print(teks6)
print(teks6.replace("o", 'a'))
print(teks2.replace("Pagi", "Malam"))
print()

# Split String (split() method)
# The split() method returns a list where the text between the specified separator becomes the list items.
teks7 = "Halo. Jangan Lupa. Semangat. Belajar"
print(teks7)
print(teks7.split("."))
print()

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this "My name is John, I am " + 36
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
umur = 20
teks8 = "Saya berumur {}"
print(teks8.format(umur))
print()

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
benar = True
teks9 = "Saya {} berumur {}"
print(teks9.format(benar, umur))
print()

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
nama = "Naufal Alwi Pratama"
teks10 = "Saya {2}, {0} berumur {1}"
print(teks10.format(benar, umur, nama))
print()

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes
teks11 = "Dia adalah orang yang 'murah senyum'"
teks12 = "Dia adalah orang yang \"murah senyum\""
print(teks11)
print(teks12)

# Untuk escape character yang lainnya bisa dilihat di dokumentasi