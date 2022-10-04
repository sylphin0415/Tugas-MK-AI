import os
os.system('cls')

print("""
            Ujian Akhir Semester
=============================================
\n
PROGRAM PYTHON MENGHITUNG NILAI MAHASISWA SEDERHANA
Input/Masukkan data mahasiswa :
=============================================""")

nama=input("Masukkan nama Mahasiswa     = ")
nim=input(str("Masukkan NIM mahasiswa       = "))
kelas=input("Masukkan kelas mahasiswa   = ")
matkul=input("Masukkan nama matakuliah mahasiswa = ")
priode=input("Masukkan priode semester mahasiswa = ")
print("===========================================\n")

print("""
Input/Masukkan nilai mahasiswa (0-100) :
==============================================""")
nPresensi=float(input("Masukkan nilai presensi mahasiswa = "))
nTugas=float(input("Masukkan nilai tugas mahasiswa = "))
nQuiz=float(input("Masukkan nilai Quiz mahasiswa = "))
nPraktek=float(input("Masukan nilai Praktikum mahasiswa = "))
nUts=float(input("Masukkan nilai UTS Mahasiswa = "))
nUas=float(input("Masukkan nilai UAS mahasiswa = "))
print("============================================")

nAbsolut=(nPresensi*10/100)+(nTugas*30/100)+(nQuiz*10/100)+(nPraktek*20/100)+(nUts*10/100)+(nUas*20/100)
if nAbsolut >= 81 :
    nRelatif="A"
    bobot=4
elif nAbsolut >= 76:
    nRelatif="B+"
    bobot=3.5
elif nAbsolut >= 66:
    nRelatif="B"
    bobot=3
elif nAbsolut >= 61:
    nRelatif="C+"
    bobot=2.5
elif nAbsolut >= 51:
    nRelatif="C"
    bobot=2
elif nAbsolut >= 26:
    nRelatif="D"
    bobot=1
elif nAbsolut >= 0:
    nRelatif="E"
    bobot=0

if nRelatif=="D" or nRelatif=="E":
    status="Tidak lulus"
else :
    status="Lulus"

print("""
Data output / Hasil
=============================================""")
print("Nama mahasiswa       =   "+nama)
print("NIM mahasiswa        =   "+nim)
print("Kelas Mahasiswa      =   "+kelas)
print("Mata Kuliah          =   "+matkul)
print("Semester             =   "+priode)
print("Nilai Absolut        =   "+str(nAbsolut))
print("Nilai Relatif        =   "+nRelatif)
print("Bobot nilai Huruf    =   "+str(bobot))
print("Status               =   "+status)