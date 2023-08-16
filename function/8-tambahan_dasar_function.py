# Untuk fungsi yang kompleks, kita bisa menggabung penulisan argument atau parameter biasa dengan arbitrary arguments (*args)
# serta arbitrary keyword arguments (**kwargs).
# Jika sebuah fungsi punya ketiga jenis argument ini, maka urutannya harus sebagai berikut:
# 1. Positional Argument Only atau Argument Biasa
# 2. Positional or Keyword Argument atau *args
# 3. Keyword Argument Only atau **kwargs
def function_kompleks(data1, data2, *data_pos_or_keyword, **data_keyword):
    print(data1, data2, data_pos_or_keyword, data_keyword)

function_kompleks(12, 13 + 2j, "Nasi", "Ikan", "Tempe", hobi="Game", kegiatan="Belajar")

print()

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the
# pass statement to avoid getting an error.
def func_kosong():
    pass

func_kosong()
print("Diatas Function Kosong\n")

# Recursion
# Python also accepts function recursion, which means a defined function can call itself
def recursif(angka):
    if angka > 1:
        hasil = angka * recursif(angka - 1)
    else:
        hasil = 1
    return hasil

print(recursif(3))