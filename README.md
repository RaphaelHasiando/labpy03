# labpy03
## latihan1.py
Tampilkan n bilangan acak yang lebih kecil dari 0.5

1. Gunakan 'from random import random'untuk membuat angka acak
2. Buatlah variable dan function input & int. Nilai N diisi pada saat runtime
###
    from random import random
    
    data = int(input("Masukkan nilai N = "))
4. Gunakan for loop untuk berapa banyak data diulangi dari data yang telah terisi.
###
    for i in range(data):
      data_random = random()
5. Pesyaratan dari Nilai random harus kuran dari 0.5, dengan menggunakan while loop (perulangan yang tak terhitung) dan if statement dapat memenuhi nilai itu secara berulang
###
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
![image](https://user-images.githubusercontent.com/61907877/141787593-7260372d-d686-46fc-95ac-4a8077405480.png)


## latihan2.py
Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.
Masukkan angka 0 untuk berhenti.

1. Gunakan variable yang berisi array (data yang dapat menampung lebih dari satu nilai)
###
    list = []
2. Gunakan while loop dan data variable yang dapat diisi saat runtime secara berulang kali
###
    list = []
    while True:
        Hs = int(input('Masukkan bilangan = '))
4. Pada saat 0, data itu langsung ditutup
###
    list = []
    while True:
        Hs = int(input('Masukkan bilangan = '))
        if Hs == 0:
            break
5. Pada saat runtime, data itu telah diisi. Menggunakan 'append()' function dapat memindahkan data yang terisi ke data array
###
    list = []
    while True:
        Hs = int(input('Masukkan bilangan = '))
        list.append(Hs)
        if Hs == 0:
            break
6. Gunakan max() funtion untuk mencari nilai yang tertinggi
###
    list = []
    while True:
        Hs = int(input('Masukkan bilangan = '))
        list.append(Hs)
        if Hs == 0:
            break
    print(f"Bilangan terbesar adalah {max(list)}")
![image](https://user-images.githubusercontent.com/61907877/141790639-5cca5938-5a95-41e4-aa21-f9de156a93df.png)

## program1.py
Buat program sederhana dengan perulangan: program1.py. Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.
1. Pertama - tama, Buatlah variable untuk modal awal, bulan, keuntungan, dan total keuntungan
###
    modal_awal = 100000000
    bulan = 0
    keuntungan = int()
    total_keuntungan = int()
2. Gunakan while loop dan pada saat diminta untuk menghitung total keuntungan selama 8 bulan
###
    while bulan < 8:
        bulan += 1
3. Dari soal deskriptif tersebut, terdapat bulan ketiga mendapatkan laba sebesar 1%, bulan kelima meningkat menjadi 5%, dan bulan kedelapan mengalami penurunan sebesar 2%
###
    while bulan < 8:
        bulan += 1
        if bulan == 3:
            keuntungan = modal_awal * 1/100
        if bulan == 5:
            keuntungan = modal_awal * 5/100
        if bulan == 8:
            keuntungan = modal_awal * 2/100
        print(f"Bulan ke-{bulan} =", keuntungan)
4. Jumlahin semua hasil keuntungannya dari bulan 1 ke 8 dengan menggunakan '+='.
###
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
![image](https://user-images.githubusercontent.com/61907877/141794091-86c1a348-c314-4ede-9342-55bd5fe87aaf.png)
