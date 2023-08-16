# Perintah return dalam function bertujuan agar sebuah function bisa mengembalikan nilai.
# Di dalam function, perintah return berfungsi mirip seperti break dalam perulangan. Jika ditemukan
# perintah return, pemrosesan function akan berhenti dan tidak akan mengeksekusi kode dibawahnya

# To let a function return a value, use the return statement
def luas_segitiga(alas:int|float, tinggi:int|float)->int|float:
    return (alas * tinggi) / 2
    print("Nasi") # Ini tidak akan dieksekusi

print("Luas segitiga dengan alas 10 cm dan tinggi 15 cm adalah ->", luas_segitiga(10, 15), "cm^2")