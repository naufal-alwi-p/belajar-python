# Arbitrary keyword arguments adalah istilah untuk menyebut jumlah named argumen fungsi yang tidak bisa ditentukan atau berubah-ubah.

# Perbedaan antara arbitrary arguments (*args) dengan arbitrary keyword arguments (**kwargs) ada di penulisan named argument atau
# named parameter.

# Jika dalam arbitrary arguments (*args) argumen fungsi ditulis langsung dengan nilai saja, maka dalam arbitrary keyword arguments
# (**kwargs), argumen fungsi tersebut ditulis dalam bentuk pasangan nama dan value. Sesampainya di dalam fungsi, parameter kwargs
# akan berbentuk tipe data dictionary.

# Sama seperti *args, nama parameter untuk **kwargs boleh bebas, tidak harus “kwargs”, namun syaratnya harus diawali dengan tanda
# bintang dua kali (**). Nama kwargs sendiri merupakan singkatan dari “keyword arguments”.

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter
# name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
def data_diri(**data):
    for i in data:
        key = i[0].upper() + i[1:]
        print(key, "=>", data[i])
    
data_diri(nama="M. Rizki", npm="01257311", prodi="Biologi", fakultas="MIPA")

print()

def tampilkan_data(**data):
    for i in data.values():
        print(i)
    
tampilkan_data(makanan="Nasi Kuning", hp="Samsung", laptop="Asus")