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
