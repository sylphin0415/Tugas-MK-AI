import os

print("""
Selamat datang di game abal abal kami :D
===========================================\n
Daftar nama : Septi, Bayu, Budi, Tono, Dika, Danu, Anto, Elga, Safi
Player 1: Buatlah nama rahasia dari daftar nama diatas! \n
""")

pilihan="1"
while pilihan == "1":
    secret=str(input("Masukkan Nama rahasia yang akan di tebak oleh player 2 (lowercase): "))
    if secret != "septi" and secret != "bayu" and secret != "budi" and secret != "tono" and secret != "dika" and secret != "danu" and secret != "anto" and secret != "elga" and secret != "safi":
        print("pilihan tidak valid")
    else:
        break

os.system('cls')

print("""
====================================================================
Player 1 sudah membuat nama yang akan ditebak, silahkan tebak :D
====================================================================""")
batas=3
for percobaan in range(batas):
    jawaban=str(input(f"Masukkan tebakanmu besti: "))
    if jawaban == secret:
        print("Selamat, tebakanmu benar besti")
        break
    else:
        print(f"Maaf besti, coba lagi...\n{batas-(percobaan+1)}x tebak lagi")
if percobaan == batas-1:
    print("Kamu cupu")
