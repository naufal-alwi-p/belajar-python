# Operator perbandingan dipakai untuk membandingkan 2 buah nilai. Hasil dari operator perbandingan ini adalah boolean True atau False.

x = 13
y = int(7)
z = float(7.0)

teks1 = "pagi"
teks2 = "Siang"

# Sama dengan (==)
print("x == y :", x == y)
print("y == z :", y == z)
print("7 == '7' :", y == '7')
print("pagi == pagi :", teks1 == "pagi")
print("pagi == Siang :", teks1 == teks2)
print("pagi == Pagi :", teks1 == "Pagi")

print()

# Tidak sama dengan (!=)
print("x != y :", x != y)
print("y != z :", y != z)
print("7 != '7' :", y != '7')
print("pagi != pagi :", teks1 != "pagi")
print("pagi != Siang :", teks1 != teks2)
print("pagi != Pagi :", teks1 != "Pagi")

print()

# Lebih besar
print('x > y :', x > y)
print("pagi > pagi :", teks1 > "pagi")
print("pagi > pergi :", teks1 > "pergi")

print()

# Lebih kecil
print('x < y :', x < y)
print("pagi < pagi :", teks1 < "pagi")
print("pagi < pergi :", teks1 < 'pergi')

print()

# Lebih besar atau sama dengan
print("x <= y :", x <= y)
print("pagi <= pagi", teks1 <= "pagi")
print("pagi <= siang", teks1 <= "siang")

print()

# Lebih kecil atau sama dengan
print("x >= y", x >= y)
print("pagi >= pagi", teks1 >= "pagi")
print("pagi >= siang", teks1 >= "siang")

# Operator perbandingan ini biasa dipakai dalam proses pengambilan keputusan atau percabangan kode program