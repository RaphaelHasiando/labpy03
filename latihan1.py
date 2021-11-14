import random

N = int(input("Masukkan nilai N = "))

for x in range(1, N + 1):
    a = random.uniform(0.0,0.5)
    print(f"Data ke {x} -> ", a)
print("Selesai")
