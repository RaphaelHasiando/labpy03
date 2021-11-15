modal_awal = 100000000
bulan = 0
keuntungan = int()
total_keuntungan = int()
while bulan < 8:
    bulan += 1
    if bulan == 3:
        keuntungan = modal_awal * 1/100
    if bulan == 5:
        keuntungan = modal_awal * 5/100
    if bulan == 8:
        keuntungan = modal_awal * 2/100
    total_keuntungan += keuntungan
    print(f"Bulan ke-{bulan} =", keuntungan)

print("Total laba adalah", total_keuntungan)
