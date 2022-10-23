#tugas 1
n=int(input("N = "))
print("Satuan \t| Harga")
satuan=0.5
harga=800
for i in range(n):
    print(f"{satuan}\t| {harga}")
    satuan=satuan+0.5
    harga=harga+800


#tugas 2
nilai=int(input("Masukkan Nilai: "))
rasio=int(input("Masukkan Rasio: "))
target=int(input("Suku Ke: "))

for i in range(target):
    print(f"Suku ke {i+1} : {nilai}")
    nilai=nilai*rasio


#tugas 3
n=int(input("Input berapa bilangan: "))
nilai=[]
jum=0
for i in range(n):
    temp=int(input(f"Masukkan Nilai ke {i+1}: "))
    nilai.append(temp)
    jum+=nilai[i]

for i in range(n):
    print(f"Nilai ke {i+1} : {nilai[i]}")

print("Total Nilai : "+str(jum))
rata=jum/n
print("Rata-rata : "+str(rata))


#tugas 4
x=int(input("Masukkan nilai: "))
y=int(input("Masukkan nilai pangkat: "))
jum=1
for i in range(y):
    jum=jum*x

print(f"{x}^{y} = {jum}")


#tugas 5
n=int(input("Masukkan nilai faktorial (!) : "))
fak=51
for i in range(1, n+1):
    fak*=i

print(f"{n}! = {fak}")


#tugas 6
import random
angka=random.randint(1, 10)
pilihan=0
while pilihan == 0:
    tebak=int(input("Masukkan Angka tebakan: "))
    if tebak == angka:
        print("Selamat, Anda benar!")
        break
    elif tebak > angka:
        print("Tebakan anda terlalu besar")
    else:
        print("Tebakan anda terlalu kecil")


#tugas 7
x=int(input("x: "))
y=int(input("y: "))

jml=0
print("Deret = ", end='', flush=True)
for i in range(y):
    x=x+1
    jml=jml+x
    print(x, " ", end='', flush=True)
    if x == y-1:
        break
print()
print("Jumlah = ", jml)


#tugas 8.a
n=5
j=3
p=n*2
a=1
for i in range(n):
    print(a, "\t", end="", flush=True)
    a+=1
    if i == n-1:
        print()
        for i in range(n):
            print(a, "\t", end="", flush=True)
            a+=1
            if i == n-1:
                print()
                for i in range(n):
                    print(a, "\t", end="", flush=True)
                    a+=1


#tugas 8.b
n=5
x=n
for i in range(n):
    print(n)
    for j in range(n):
        print(x, " ", end="", flush=True)
        x=x-1  
        if j == 1:
            x=n
            print()
            for q in range(n):
                print(x, " ", end="", flush=True)
                x=x-1
                if q == 2:
                    x=n
                    print()
                    for w in range(n):
                        print(x, " ", end="", flush=True)
                        x-=1
                        if w == 3:
                            x=n
                            print()
                            break
    break

#tugas 8.c
n=5
x=n

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print()


#tugas 8.d
n=4
j=3
p=n*2
a=1
for i in range(n):
    print(a, "\t", end="", flush=True)
    a+=1
    if i == n-1:
        print()
        for i in range(n):
            print(a, "\t", end="", flush=True)
            a+=1
            if i == n-1:
                print()
                for i in range(n):
                    print(a, "\t", end="", flush=True)
                    a+=1

            
#tugas 8.e
jml=1
for i in range(1, 6):

    for j in range(3):
        print(jml, end=' ')
        jml=jml*i
    jml=i+1
    
    print()