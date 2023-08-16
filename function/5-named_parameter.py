# Named parameter adalah istilah programming untuk menyebut cara pengiriman nilai dari argumen ke parameter function dengan
# menulis nama parameter, tidak sekedar nilainya saja. Named parameter ini sering juga disebut sebagai named argument atau
# keyword arguments.

# Dengan menggunakan named parameter, kita tidak harus bergantung kepada urutan parameter pada saat menjalankan sebuah fungsi.
# Urutan argumen bisa ditulis acak selama nama argumen sama dengan nama parameter

# You can send arguments with the key = value syntax. This is called Keyword Argument/Named Parameter
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def sapa(nama, hobi, makanan):
    print(nama, "mempunyai hobi", hobi.lower(), "dan makanan kesukaannya adalah", makanan.lower())

sapa("Azka", "Olahraga", "Pizza")
sapa(makanan="Soto Ayam", nama="Ardian", hobi="Sepak Bola") # Memanggil function dengan named parameter