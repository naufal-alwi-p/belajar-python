# Biasanya sebuah fungsi bisa menerima nilai masukan atau nilai input. Nilai masukan inilah yang dimaksud dengan parameter atau argumen.
# Information can be passed into functions as arguments.

# A parameter is the variable listed inside the parentheses in the function definition.
# Parameter adalah sebutan untuk nilai inputan fungsi pada saat fungsi itu di definisikan
def perkalian(a:int | float | complex, b:int | float | complex)->int | float | complex: # Variabel a dan b adalah parameter
    print(a * b)


# An argument is the value that is sent to the function when it is called.
# Arguments are often shortened to args in Python documentations.
# Argumen adalah sebutan untuk nilai inputan fungsi pada saat fungsi itu dipanggil.
perkalian(5.1, 2 + 2j) # Nilai 2.5 dan 2 adalah argumen

def luas_segitiga(alas: int | float, tinggi: int | float):
    print(alas * tinggi / 2)

luas_segitiga(10, 15)