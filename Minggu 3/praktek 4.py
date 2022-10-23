#Program 1

title="Program Penilaian Mahasiswa"
line="-"*50
listnama=[]
listnilai=[]
batas = 5
total=0
print(title.center(50))
print(line)
for i in range(batas):
    nama=input("Masukkan nama\t= ")
    nilai=int(input("Masukkan nilai\t= "))
    total=total+nilai
    listnama.append(nama)
    listnilai.append(nilai)
    print()
print(line)
rtrt=total/len(listnilai)
print("No\tNama\tNilai")
print(line)
for j in range(batas):
    print(f"{j+1}\t{listnama[j]}\t{listnilai[j]}")
print(line)
print("Jumlah Mahasiswa = ", len(listnama))
print("Rata - rata = ", rtrt)


#Program 2.a
title="Program Penilaian Mahasiswa"
line="-"*50
listnama=[]
listnilai=[]
listlulus=[]
listgagal=[]
batas = 5
total=0
print(title.center(50))
print(line)
for i in range(batas):
    nama=input("Masukkan nama\t= ")
    nilai=int(input("Masukkan nilai\t= "))
    total=total+nilai

    listnama.append(nama)
    listnilai.append(nilai)
    print()

dict1=dict(zip(listnilai, listnama))



print(line)
rtrt=total/len(listnilai)
print("No\tNama\tNilai")
print(line)
for j in range(batas):
    print(f"{j+1}\t{listnama[j]}\t{listnilai[j]}")
print(line)
print("Jumlah Mahasiswa = ", len(listnama))
print("Rata - rata = ", rtrt)
print(f"Nilai Tertinggi = {max(dict1)} oleh {dict1[max(dict1)]}")
print(f"Nilai Terendah = {min(dict1)} oleh {dict1[min(dict1)]}")



#Program 2.b
title="Program Penilaian Mahasiswa"
line="-"*50
listnama=[]
listnilai=[]
listlulus=[]
batas = 5
total=0
lulus=0
gagal=0
print(title.center(50))
print(line)
for i in range(batas):
    nama=input("Masukkan nama\t= ")
    nilai=int(input("Masukkan nilai\t= "))
    total=total+nilai
    if nilai >= 60:
        lulus+=1
        keterangan="Lulus"
    else:
        gagal+=1
        keterangan="Tidak Lulus"
    listlulus.append(keterangan)
    listnama.append(nama)
    listnilai.append(nilai)
    print()

dict1=dict(zip(listnilai, listnama))

print(line)
rtrt=total/len(listnilai)
print("No\tNama\tNilai\tKeterangan")
print(line)

for j in range(batas):
    print(f"{j+1}\t{listnama[j]}\t{listnilai[j]}\t{listlulus[j]}")


print(line)
print()
print("Jumlah Mahasiswa = ", len(listnama))
print("Rata - rata = ", rtrt)
print(f"Nilai Tertinggi = {max(dict1)} oleh {dict1[max(dict1)]}")
print(f"Nilai Terendah = {min(dict1)} oleh {dict1[min(dict1)]}")
print(f"Jumlah lulus = {lulus}")
print(f"Jumlah Gagal = {gagal}")


#program 3
listnama=[]
listtugas=[]
listuts=[]
listuas=[]
listna=[]
jumtugas=0
jumuts=0
jumuas=0
jumna=0
title="NILAI MAHASISWA"
line="-"*50


banyak=int(input("Jumlah Mahasiswa= "))
for i in range(banyak):
    nama=input("Masukkan nama = ")
    tugas=int(input("Masukkan nilai Tugas = "))
    uts=int(input("Masukkan nilai UTS = "))
    uas=int(input("Masukkan nilai UAS = "))
    jumtugas=jumtugas+tugas
    jumuts=jumuts+uts
    jumuas=jumuas+uas
    na=(30/100)*tugas+30/100*uts+40/100*uas
    jumna=jumna+na
    listnama.append(nama)
    listtugas.append(tugas)
    listuts.append(uts)
    listuas.append(uas)
    listna.append(na)
    print()

rttugas=jumtugas/len(listtugas)
rtuts=jumuts/len(listuts)
rtuas=jumuas/len(listuas)
rtna=jumna/len(listna)
rtna=int(rtna)

print(line)
print("No\tNama\tTugas\tUTS\tUAS\tNA")
print(line)
for j in range(banyak):
    print(f"{j+1}\t{listnama[j]}\t{listtugas[j]}\t{listuts[j]}\t{listuas[j]}\t{listna[j]}")
print(line)
print(f"Rata-rata\t{rttugas}\t{rtuts}\t{rtuas}\t{rtna}")
print(line)


#tugas 4
listgenap=[]
n=5
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    if nilai%2==0:
        listgenap.append(nilai)
print("Bilangan genap = ", listgenap)

#tugas 5
listbil=[]
n=5
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    listbil.append(nilai)
print("Bilangan Terbesar = ", max(listbil))


#program 6.a
listgenap=[]
n=5
for i in range(n):
    nilai=int(input(f"Masukkan nilai ke {i+1}= "))
    listgenap.append(nilai)
print()
for j in range(n):
    if j%2==0:
        print(f"Bilangan  di indeks {j} = {listgenap[j]}")


#program 6.b
listpositif=[]
n=5
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    if nilai>0:
        listpositif.append(nilai)
print()
print("Bilangan positif = ", listpositif)


#program 6.c
listbil=[]
n=5
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    if nilai%2==1 and nilai%3==0:
        listbil.append(nilai)
print()
print("Bilangan ganjil dan kelipatan 3 = ", listbil)


#program 6.d
listbil=[]
n=5
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    if nilai%3!=0:
        listbil.append(nilai)
print()
print("Bilangan yang tidak habis di bagi 3 = ", listbil)


#program 7
listbil=[]
n=int(input("Masukkan banyak bilangan: "))
for i in range(n):
    nilai=int(input("Masukkan nilai = "))
    if nilai%5==0:
        listbil.append(nilai)
print()
print("Bilangan kelipatan 5 = ", listbil)


#program 8
import numpy as np

a=[]
b=[]
for i in range(3):
    nilai=int(input("Masukkan untuk nilai a : "))
    a.append(nilai)
for j in range(3):
    nilai=int(input("Masukkan untuk nilai b : "))
    b.append(nilai)
c=np.dot(a,b)



#program 9
list=[]
jml=0
x=int(input("Masukkan banyak data = "))
for i in range(x):
    nilai=int(input(f"Masukkan Nilai index {i} ="))
    jml+=nilai
    list.append(nilai)
print(jml)


#program 10
listpositif=[]
listnegatif=[]
x=int(input("Masukkan banyak data = "))
for i in range(x):
    nilai=int(input(f"Masukkan nilai ke {i+1} = "))
    if nilai>0:
        listpositif.append(nilai)
    else:
        listnegatif.append(nilai)

if len(listpositif)>len(listnegatif):
    print("Bilangan positif lebih banyak")
else:
    print("Bilangan negatif lebih banyak")


#program 11
import numpy as np
matriks = np.random.random_integers(1, 4,(2, 2))
print("a: ")
print (matriks)
matriks2 = np.random.randint(1, 4,(2, 2))
print()
print("b: ")
print (matriks2)
matrik_kali=np.dot(matriks, matriks2)
print()
print("Hasil perkalian: ")
print (matrik_kali)




#program 12
a=(1,2,3,4,5)
b=list(a)
c=int(input("Masukkan skalar: "))
for i in range(len(a)):
    b[i]=b[i]*c
a=tuple(b)
print(a)



#program 13
dictsatu={"nim":"12345678", "nama":"Fatih", "IPK":"3.90"}
dictDua={"hobi":"main Bola", "alamat":"Bandung"}

dictgabung={**dictsatu, **dictDua}
for x, y in dictgabung.items():
    print (x, "\t:\t", y)   
