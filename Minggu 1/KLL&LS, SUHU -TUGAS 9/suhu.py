import os
print('''
==============================
        KONVERSI SUHU
==============================''')
pilihan = 'y'
while pilihan == 'y':
    print('''
====================================
Pilih konverter:
1. fahrenheit > celcius
2. celcius > reamur
3. celcius > fahrenheit
4. reamur > celcius
5. Exit''')
    suhu=int(input('Masukkan pilihan: '))
    if suhu == 5:
        print('EXIT...')
        break
    elif suhu > 5 or suhu < 1:
        print('Pilihan Tidak Valid')
        pilihan=input("Konversi lagi (y/n)? ")
        if pilihan == "n":
            break
        else: 
            os.system('cls')
    else:
        derajat1=int(input("Masukkan derajat: "))
        if suhu == 1:
            hasil=(derajat1-32)*(5/9)
            print(f'{derajat1} °F = {hasil} °C')
        elif suhu == 2:
            hasil=(4/5)*derajat1
            print(f'{derajat1} °C = {hasil} °R')
        elif suhu == 3:
            hasil=(derajat1*(9/5))+32
            print(f'{derajat1} °C = {hasil} °F')
        elif suhu == 4:
            hasil=(5/4)*derajat1
            print(f'{derajat1} °R = {hasil} °C')
        else:
            print()
    pilihan=input("Konversi lagi (y/n)? ")
    if pilihan == 'n':
        print('EXIT...')
        break
    else:
        os.system('cls')
#RIZKI NURHAFIZD ACHMAD
#211001114