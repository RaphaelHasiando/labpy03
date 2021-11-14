list = []
while True:
    Hs = int(input('Masukkan bilangan = '))
    list.append(Hs)
    if Hs == 0:
        break
print(f"Bilangan terbesar adalah {max(list)}")
