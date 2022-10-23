#PROGRAM 0
title="UNIVERSITAS KOMPUTER INDONESIA"
subtitle="Jl Dipati Ukur 112-114, Bandung"
line="-"*100
nama="Oemar Bakri"
nim="10205088"
jurusan="Teknik Komputer"
fakultas="Teknik dan  Ilmu Komputer"
print(title.center(100))
print(subtitle.center(100))
print(line)
print("Nama         : "+nama)
print("NIM          : "+nim)
print("Jurusan      : "+jurusan)
print("Fakultas     : "+fakultas)
print(line)


#PROGRAM 1
title="DATA KECEPATAN MOBIL"
line="-"*100
print(title.rjust(100))
print(line)
v=float(input("Kecepatan rata-rata(Km/Jam)    : "))
t=float(input("Waktu Tempuh (jam)             : "))
s=v*t
print("Jarak tempuh                   : "+str(s)+"km")
print(str(v)+"x"+str(t)+"="+str(s)+"km")


#PROGRAM 2
print("""
            Program Menghitung Pembelian
-----------------------------------------------------
""")
harga=10000
print("Harga Satuan         : Rp 10.000")
jumlah_beli=input("Jumlah Pembelian         : ")
diskon=10/100
harga_total=harga*jumlah_beli*diskon
print(f"Harga Total             : Rp {harga_total}")


#PROGRAM 3
title="PROGRAM PENJUALAN BUKU"
line="-"*50
print(title.center(50))
print(line)
satuan=int(input("Harga Satuan            : "))
jml=int(input("Jumlah Pembelian        : "))
dskn=int(input("Diskon                  : "))
harga=(satuan*jml)*dskn/100
harga_total=(satuan*jml)-harga
print(f"Harga Total             : Rp.{harga_total}")
print(line)



#PROGRAM 4
title="PROGRAM MENGHITUNG TAGIHAN TELEPON"
line="-"*50
print(title.center(50))
print(line)
print("DATA PELANGGAN")
nama=input("Nama Pelanggan                      : ")
percakapan=int(input("Percakapan                          : "))
sms=int(input("SMS                                 : "))
print()
print("TAGIHAN")
abonemen=20000
bPercakapan=percakapan*1000
bSms=sms*300
total=abonemen+bPercakapan+bSms
print(f"Abonemen                         : Rp {abonemen}")
print(f"Biaya Percakapan                 : Rp {bPercakapan}")
print(f"Biaya SMS                        : Rp {bSms}")
print(line)


#PROGRAM 5
line="-"*100
title="PROGRAM GAJI PEGAWAI"
print(title.center(100))
print(line)
nama=input("Nama Karyawan       : ")
anak=int(input("Jumlah anak     : "))
gj_pokok=float(input("Gaji Pokok    :"))
print(line)
print(f"|Gaji Pokok\t|\tT.Kesejahteraan\t|\tT.Keluarga\t|\tPajak|")
sejahtera=20/100*gj_pokok
keluarga=(10/100*gj_pokok)*anak
gj_kotor=gj_pokok+sejahtera+keluarga
pajak=gj_kotor*10/100
print(f"|{gj_pokok}\t|\t{sejahtera}\t|\t{keluarga}\t|\t{pajak}|")
print(line)
print("Gaji Kotor   : "+str(gj_kotor))
print("Gaji Bersih  : "+str(pajak))


#Program 6
line="-"*75
nilai=int(input("Nilai Uang: "))
print(line)
ribu=nilai/1000
ribu=int(ribu)
convert_ribu=nilai-ribu*1000
ratus=convert_ribu/200
ratus=int(ratus)
convert_ratus=convert_ribu-ratus*200
puluh=convert_ratus/50
puluh=int(puluh)
print(f"{nilai} Rupiah : {ribu} (Seribuan) + {ratus} (Dua Ratusan) + {puluh} (Lima Puluhan)")



#Program 7
title="KEUANGAN"
line="-"*50
print(title.center(50))
print(line)
gaji=int(input("Gaji\t= "))
hutang=int(input("Hutang\t= "))
bersih=gaji-hutang
sehari=bersih*(70/100)
tabung=bersih*(20/100)
infak=bersih*(10/100)
print(f"Biaya Sehari^^\t= {sehari}")
print(f"Tabungan\t= {tabung}")
print(f"Infak\t\t= {infak}")
