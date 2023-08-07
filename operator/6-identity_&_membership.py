# Operator identitas adalah operator yang bisa dipakai untuk memeriksa apakah nilai sebuah variabel ada di tempat yang
# sama (di memory) atau tidak. Operator ini dikenal juga sebagai identity operators.

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same
# object, with the same memory location

# Operator ini terdiri dari 2 jenis:
# is:     Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai yang sama
# is not: Bernilai True jika kedua operand merujuk ke object yang tidak sama

# Untuk tipe data dasar seperti number atau string, jika dua buah variabel berisi nilai yang sama, maka operator
# is akan menghasilkan nilai True.
teks1 = "Pagi"
teks2 = 'Pagi'

print('teks1 is teks2:', teks1 is teks2)
print('teks1 is not teks2:', teks1 is not teks2)
print()

angka1 = 75
angka2 = 75

print('angka1 is angka2:', angka1 is angka2)
print('angka1 is not angka2:', angka1 is not angka2)
print()

bkoma1 = 21.3
bkoma2 = 21.3

print('bkoma1 is bkoma2:', bkoma1 is bkoma2)
print('bkoma1 is not bkoma2:', bkoma1 is not bkoma2)
print()

imaji1 = 13 + 5j
imaji2 = 13 + 5j

print('imaji1 is imaji2:', imaji1 is imaji2)
print('imaji1 is not imaji2:', imaji1 is not imaji2)
print()

benar1 = True
benar2 = True

print('benar1 is benar2:', benar1 is benar2)
print('benar1 is not benar2:', benar1 is not benar2)
print()

# Namun untuk tipe data lain seperti list. Meskipun nilai element-nya sama persis, tapi
# Python menyimpannya di alamat memory yang berbeda, sehingga dianggap tidak identik.
hobi1 = ['Belajar', 'Makan', 'Game']
hobi2 = ['Belajar', 'Makan', 'Game']

print('hobi1 is hobi2:', hobi1 is hobi2)
print('hobi1 is not hobi2:', hobi1 is not hobi2)
print()

cek1 = {3: "Tahu", "Kota": "Medan"}
cek2 = {3: "Tahu", "Kota": "Medan"}

print(cek1 is cek2)
print(cek1 is not cek2)
print()

# Operator keanggotaan adalah operator yang dipakai untuk memeriksa apakah suatu nilai ada di dalam sebuah himpunan atau tidak.
# Himpunan yang dimaksud terdiri dari tipe data “berbentuk array” seperti string, list, tuple, set dan dictionary. Operator
# ini dikenal juga sebagai membership operators.

# Operator ini terdiri dari 2 jenis:
# in:     Bernilai True jika nilai yang dicari ada di dalam himpunan
# not in: Bernilai True jika nilai yang dicari tidak ada dalam himpunan

kalimat = "Pagi hari bersinar dan bercahaya"

print('"dan" in kalimat:', "dan" in kalimat)
print('"tahu" not in kalimat:', "tahu" not in kalimat)
print()

catat = [12, 102, 237, 87, 65, [54, 23]]

print('[54, 23] in catat:', [54, 23] in catat)
print('102 in catat:', 102 in catat)
print('102 not in catat:', 102 not in catat)
