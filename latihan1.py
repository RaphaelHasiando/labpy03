from random import random

data = int(input("Masukkan nilai N = "))
x = 0

for i in range(data):
    data_random = random()
    while True:
        if data_random < 0.5:
            print(f"Data ke {i + 1} =", data_random)
        break

print("Selesai")
