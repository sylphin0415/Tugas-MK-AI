#program 1
def rumus():
    print("""
    Pilihan:
    1. Persegi panjang
    2. Segitiga
    3. Lingkaran
    """)

    pilihan=input("Pilihan = ")
    pilihan=pilihan.capitalize()
    if pilihan=="Persegi panjang" or pilihan=="1": 
        p=int(input("Masukkan nilai panjang: "))
        l=int(input("Masukkan nilai lebar: "))
        luas=p*l
        print(f"Luas : {luas}")
    elif pilihan=="2" or pilihan=="Segitiga":
        a=int(input("Masukkan nilai Alas: "))
        t=int(input("Masukkan nilai tinggi: "))
        luas=(1/2)*a*t
        print(f"Luas : {luas}")
    elif pilihan=="3" or pilihan=="Lingkaran":
        r=int(input("Masukkan nilai jari-jari: "))
        luas=3.14*r*r
        print(f"Luas : {luas}")

rumus()


#Program 2
def Persegi_panjang():
    p=int(input("Masukkan nilai panjang: "))
    l=int(input("Masukkan nilai lebar: "))
    luas=p*l
    print(f"Luas : {luas}")

def Segitiga():
    a=int(input("Masukkan nilai Alas: "))
    t=int(input("Masukkan nilai tinggi: "))
    luas=(1/2)*a*t
    print(f"Luas : {luas}")

def Lingkaran():
    r=int(input("Masukkan nilai jari-jari: "))
    luas=3.14*r*r
    print(f"Luas : {luas}")

print("""
    Pilihan:
    1. Persegi panjang
    2. Segitiga
    3. Lingkaran
    """)
pilihan=input("Pilihan = ")
pilihan=pilihan.capitalize()
if pilihan=="Persegi panjang" or pilihan=="1": 
    Persegi_panjang()
elif pilihan=="2" or pilihan=="Segitiga":
    Segitiga()
elif pilihan=="3" or pilihan=="Lingkaran":
    Lingkaran()


#program 3
def LuasSgt(alas, tinggi):
    luas=(1/2)*alas*tinggi
    print(f"Luas : {luas}")

x=int(input("Masukkan nilai alas: "))
y=int(input("Masukkan nilai tinggi: "))
LuasSgt(x, y)


#Program 4
def InputData():
    list1=[]
    banyak=int(input("Masukkan banyak data: "))
    for i in range(banyak):
        nilai=int(input(f"Masukkan nilai ke {i+1}: "))
        list1.append(nilai)
    return list1


def Proses(list):
    print(list)
    a=max(list)
    return a


def CetakHasil(a):
    print(f"Nilai maksimal: {a}")

def main():
    return_list=InputData()

    a=Proses(return_list)
    CetakHasil(a)

main()


#Program 5
def InputData(banyak):
    list1=[]
    for i in range(banyak):
        nilai=int(input(f"Masukkan nilai ke {i+1}: "))
        list1.append(nilai)
    return list1


def Proses(list):
    nilai=[]
    x=int(input("Mencari kelipatan dari: "))
    for i in range(len(list)):
        if list[i]%x==0:
            nilai.append(list[i])
    print(f"No Indeks\tBilangan kelipatan {x}")
    return nilai


def CetakHasil(a):
    for i in range(len(a)):
        print(f"{i}\t\t{a[i]}")


def main():
    n=int(input("Masukkan banyak data: "))
    return_list=InputData(n)
    a=Proses(return_list)
    CetakHasil(a)

pilihan=0
while pilihan==0:
    main()
    lanjut=input("Ulang lagi (y/t)? ")
    if lanjut=="t":
        break


#Program 6
def faktorial(n):
    jum=1
    for i in range(n):
        jum=jum*(i+1)
    return jum

fak=int(input("Masukkan bilangan faktorial = "))
n = faktorial(fak)
print(f"Faktorial dari {fak}! = {n}")


#program 7
