import random

N = int(input("Masukkan Jumlah N: "))

for i in range(1, N + 1):
    a = random.uniform(0.0,0.5)
    print(f"Data ke {i} -> ", a)
print("Selesai")
