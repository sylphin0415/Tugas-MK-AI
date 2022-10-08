import os
os.system('cls')
print("""
===================================
            Kalkulator
===================================
""")
pilihan = "yes"
while pilihan == "yes" :
    print("""
======================================
1. +
2. -
3. *
4. /
0. Keluar
====================================== 
""")
    operasi=int(input("Masukan operasi: "))
    if operasi == 1:
        angka1=int(input("Masukkan angka pertama: "))
        angka2=int(input("Masukkan angka kedua: "))
        print(f"{angka1} + {angka2} = {angka1+angka2}")
    elif operasi == 2:
        angka1=int(input("Masukkan angka pertama: "))
        angka2=int(input("Masukkan angka kedua: "))
        print(f"{angka1} - {angka2} = {angka1-angka2}")
    elif operasi == 3:
        angka1=int(input("Masukkan angka pertama: "))
        angka2=int(input("Masukkan angka kedua: "))
        print(f"{angka1} x {angka2} = {angka1*angka2}")
    elif operasi == 4:
        angka1=int(input("Masukkan angka pertama: "))
        angka2=int(input("Masukkan angka kedua: "))
        if angka2 == 0:
            print("Tidak bisa di bagi 0 [INVALID]")
        else :
            print(f"{angka1} / {angka2} = {angka1/angka2}")
    elif operasi == 0:
        print("Program Keluar")
    else:
        print("Perintah tidak dikenal")
    lagi=input("Menghitung lagi? (y/n) ")
    if lagi == 'y':
        os.system('cls')
    else:
        operasi=0
        print('Program Selesai')
        break
#RIZKI NURHAFIZD ACHMAD
#211001114
