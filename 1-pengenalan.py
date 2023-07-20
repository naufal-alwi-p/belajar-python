# Ini cara membuat Comment di Python

# Python tidak butuh ";" untuk menandakan akhir statement
# Python menggunakan karakter new line untuk menandakan akhir statement
# Meskipun begitu kita masih bisa menggunakan ";" untuk menunjukkan akhir statement

# Penamaan pada Python bersifat vase-sensitive (huruf besar dan kecil berbeda)

# Kita tidak perlu mendeklarasikan variabel, langsung inisialisasi saja
# Tipe data dalam Python tidak begitu "strict" seperti C/C++
a = "Hello World"
# Tampilkan nilai variabel a
print(a)

a = 12.7
print(a)

# Python tidak punya Konstanta
# Untuk mengatasi hal ini, kesepakatan programmer Python adalah dengan membuat nama variabel dalam huruf besar untuk menandakan sebuah konstanta
PI = 3.14
print(PI)

# Type Casting
a = str(a)
print(a, "adalah string")

# Cek Tipe Data
print(type(a))

# Banyak Nilai ke Banyak Variabel
q, w, e = 12, "Nasi", True
print(q, w, e)

# Satu Nilai ke Banyak Variabel
p = o = i = 657
print(p, o, i)

# Dalam javascript ini disebut destructuring (dalam python disebut unpack)
f, g, h = [12, 54, 43]
print(f, g, h)

# Dalam Python indentasi menunjukkan block scope (dalam pemrograman turunan C/C++ block scope ditunjukkan oleh {})
if(p > 100):
    print(p, "lebih besar dari 100")

# Global Variabel adalah variabel yang dibuat di lingkungan global
# Local Variabel adalah variabel yang dibuat di dalam function
teks = "Ini Variabel Global"

def tesFunction():
    print(teks)

def tesFunc():
    teks = "Ini Variabel Lokal"
    print(teks)

def tesFunc2():
    global teks2 # Deklarasi dulu
    teks2 = "Ini dibuat di local scope, tapi bisa diakses di global" # Baru inisialisasi
    print(teks2)

def tesFunc3():
    global teks # Deklarasi dulu
    teks = "Varibel teks bisa diubah dalam local scope dengan memanggilnya di dalam local scope dengan keyword global" # Baru inisialisasi

print("")
print("--------------------------------------------------------------------------------------------------")
print("")

print(teks)

tesFunction()

tesFunc()

tesFunc2()
print(teks2)

tesFunc3()
print(teks)