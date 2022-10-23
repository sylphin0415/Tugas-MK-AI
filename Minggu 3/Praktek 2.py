
x=int(input("Nilai x: "))
y=int(input("Nilai y: "))
if x>y:
    print(f"{x} Adalah nilai terbesar")
else:
    print(f"{y} Adalah nilai terbesar")


x=int(input("Nilai x: "))
y=int(input("Nilai y: "))
z=int(input("Nilai z: "))
if x>y and x>z:
    print(f"{x} Adalah nilai terbesar")
elif y>x and y>z:
    print(f"{y} Adalah nilai terbesar")
else:
    print(f"{z} Adalah nilai tersebar")


x=int(input("Nilai x: "))
y=int(input("Nilai y: "))
z=int(input("Nilai z: "))
if x==y:
    print(f"x({x}) = y({y})")
elif x==z:
    print(f"x({x}) = z({z})")
elif y==z:
    print(f"y({y}) = z({z})")
else:
    print("Tidak ada angka yang sama")


nama=input("Nama Anda\t= ")
tinggi=int(input("Tinggi\t\t= "))
ideal=tinggi-100
print(f"Saudara {nama}, berat ideal anda adalah {ideal} kg")


title="DATA NILAI MAHASISWA"
line="-"*50
print(title.center(50))
print(line)
nama=input("Nama\t\t= ")
tugas=float(input("Tugas\t\t= "))
uts=float(input("UTS\t\t= "))
uas=float(input("UAS\t\t= "))
print(line)

title="NILAI AKHIR DAN GRADE"
print(title.center(50))
print(line)
na=float((25/100)*tugas+(35/100)*uts+(40/100*uas))
print(f"Nama\t\t: {nama}")
print(f"Nilai Akhir\t: {na}")


if na >= 75:
    grade="A"
elif na >= 60:
    grade="B"
elif na >= 45:
    grade="C"
elif na < 45:
    grade="D"
print(f"GRADE\t\t: {grade}")
print(line)


title="DATA PEGAWAI"
line="-"*50
print(title.center(50))
print(line)
nama=input("Nama\t\t: ")
gol=input("Golongan\t: ")
jam=int(input("Total Jam Kerja\t: "))
print(line)
print()
gol=gol.upper()
if gol == "A":
    gaji_pokok=500000
    tunjangan=gaji_pokok*(10/100)
    lembur=5000
elif gol == "B":
    gaji_pokok=700000
    tunjangan=(gaji_pokok*(15/100))
    lembur=7500
elif gol == "C":
    gaji_pokok=900000
    tunjangan=(gaji_pokok*(20/100))
    lembur=10000

if jam > 200:
    kerja=jam-200
    total=gaji_pokok+tunjangan+(lembur*kerja)
else:
    total=gaji_pokok+tunjangan

title="PERHITUNGAN GAJI"
print(title.center(50))
print(line)
print(f"Gaji Pokok\t: {gaji_pokok}")
print(f"Tunjangan\t: {tunjangan}")
print(f"lembur\t\t: {kerja}")
print(line)
print(f"Total\t\t: {total}")


