# Default Parameter adalah istilah untuk parameter yang memiliki nilai awal, atau nilai default. Kadang fitur ini disebut juga
# sebagai Default Argument.

# If we call the function without argument, it uses the default value
def sapa(nama, waktu = 'Pagi'): # Variabel waktu merupakan default parameter
    print("Halo", nama + ", Selamat", waktu)

sapa("Randi")
sapa("Rizki", 'Sore')

# Dengan nilai default ini, kita bisa merancang fungsi dengan parameter yang bersifat opsional. Parameter bisa diisi pada saat
# pemanggilan fungsi, namun boleh juga diabaikan.

# Fitur default parameter bisa dimanfaatkan untuk membuat fungsi yang fleksibel, karena pada saat pemanggilan fungsi kita tidak
# harus menginputkan seluruh parameter, tetapi apa yang dianggap perlu saja.

# Sebuah fungsi bisa memiliki banyak default parameter, namun tidak boleh ada parameter tanpa nilai default yang ditulis setelah
# parameter dengan nilai default. (function dibawah akan error)
# def jumlah(a, b = 0, c):
#     print(a + b + c)