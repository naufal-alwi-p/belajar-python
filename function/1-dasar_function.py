# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Pada saat merancang kode program, kadang kita sering membuat kode yang melakukan tugas sama secara berulang-ulang
# Tugas yang sama ini akan lebih efektif jika dipisahkan dari program utama dan dirancang menjadi sebuah fungsi atau function.

# Dalam penamaan function, berdasarkan PEP – 8 (Python Enhancement Proposal) yang berisi tata cara penamaan yang disarankan. 
# Dalam dokumen tersebut, nama function sebaiknya ditulis dengan huruf kecil semua dan menggunakan underscore (_) sebagai pemisah kata.
# Aturan penamaan ini sering disebut sebagai snake_case()
# Ketika sebuah function di definisikan, function tersebut belum berjalan. Disini kita hanya memberitahu interpreter bahasa Python
# bahwa sebuah function sudah disiapkan.
# Agar bisa berjalan, sebuah function harus “dipanggil” dengan cara menulis nama fungsi tersebut diakhiri dengan ()

# In Python a function is defined using the def keyword
def sapa_pagi():
    print("Selamat Pagi")

# To call a function, use the function name followed by parenthesis ()
sapa_pagi()
sapa_pagi()
sapa_pagi()

print()

# Kita juga bisa membuat variabel di dalam function
def sapa_siang():
    teks = 'Selamat Siang'
    print(teks)

sapa_siang()
sapa_siang()
sapa_siang()
