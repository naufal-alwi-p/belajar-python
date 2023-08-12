# With the while loop we can execute a set of statements as long as a condition is true.

# Python tidak punya increment/decrement operator contoh: i++ dan i--
# Sebagai alternatif gunakan i += 1 dan i -= 1

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
i = 1

while i <= 10:
    print(i)
    i += 1

print("\n" + str(i))

# With the break statement we can stop the loop even if the while condition is true
i = 1

while i < 100:
    print("Perulangan ke-" + str(i))
    if i == 5:
        break
    i += 1

print()

# With the continue statement we can stop the current iteration, and continue with the next
i = 0

while i < 7:
    i += 1
    if i == 4:
        continue
    print("Perulangan ke-" + str(i))

print()

# With the else statement we can run a block of code once when the condition no longer is true
i = 0

while i <= 10:
    i += 1
    if (i % 2) != 0:
        continue
    print(i)
else:
    print("Sudah selesai perulangannya")

print()

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
i = 1

while i < 10:
    if i == 6:
        break
    print(i)
    i += 1
else:
    print("Ini akan dijalankan jika perulangan tidak dihentikan oleh break")

print()

# A nested loop is a loop inside a loop.
i = 0

while i < 3:
    j = 1
    while j <= 5:
        print(i, "=>", j)
        j += 1
    i += 1

print()

# Tambahan
tuple1 = ("Angka", 43, True, "Indonesia", 12 + 6j)
i = 0

while i < len(tuple1):
    print(tuple1[i])
    i += 1