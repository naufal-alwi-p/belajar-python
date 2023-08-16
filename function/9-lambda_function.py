# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax= lambda arguments : expression
# The expression is executed and the result is returned

jumlah = lambda x=0, y=0:x + y

print(jumlah(12, 7))

print()

def beri_function():
    '''Function Ini Mengembalikan Anonymus (lambda) function

    Anonymus (lambda) function yang dikembalikan berfungsi untuk  memproses perkalian dua bilangan
    '''
    return lambda x, y : x * y

perkalian = beri_function()

print(perkalian(y=12, x=3))

# Tambahan
# lambda function bisa menerima default parameter, named parameter, *args, **kwargs, dll
# Intinya hampir semua fitur yang dimiliki function biasa, bisa juga untuk lambda function
# Hanya saja, lambda function dibatasi hanya bisa untuk 1 expression saja
