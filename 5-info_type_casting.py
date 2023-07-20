# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated
# language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal
# (providing the string represents a whole number)
num1 = int(21.6)
num2 = int("175")
print(type(num1), num1)
print(type(num2), num2)

# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents
# a float or an integer)
f1 = float(47)
f2 = float("75.864")
print(type(f1), f1)
print(type(f2), f2)

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
teks1 = str(576)
teks2 = str(12.6 + 12j)
print(type(teks1), teks1)
print(type(teks2), teks2)

# Lebih Lengkap Lihat 2-tipe_data_dgn_constructor.py
