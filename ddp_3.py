#N0 1 Profil Pribadi 
nama,nim,kelas,noTelp,alamat="Putri Salwa","0110124098","SI07","0895339069967","Perumahan Greenery Permai Blok D14 Rt 07 Rw 07"
print("Nama Mahasiswa", nama)
print("Nim Mahasiswa", nim)
print("Kelas Mahasiswa", kelas)
print("NoTelp Mahasiswa", noTelp)
print("Alamat Mahasiswa", alamat)

print("===Profil===")

#No 2 Profil Teman
nama,nim,kelas,noTelp,alamat="Najwa Lutfiah","0110124151","SI09","0895635109645","Jln.Tridharma leman,Rt05 Rw04,meruyung limo"
print("Nama Mahasiswa", nama)
print("Nim Mahasiswa", nim)
print("Kelas Mahasiswa", kelas)
print("NoTelp Mahasiswa", noTelp)
print("Alamat Mahasiswa", alamat)

print("===Profil Teman===")


#No 3 Mencari Tinggi Badan dan Berat Badan 
tb=int(input("Masukkkan Tinggi Badan:"))
bbideal=(tb-100)-((tb-100)*0.15)
print("Berat Badan Ideal dengan Tinggi Badan" ,tb, "adalah",bbideal,"kg")
print(type(bbideal))

print("===bbideal===")

#No 4 Mencari Celcius ke fahreinheit
celcius=float(input("masukkan nilai celcius:"))
fahreinheit=(celcius*9/5)+32
print(celcius,"derajat celcius sama  dengan",fahreinheit,"derajat fahreinheit")

print("===Celcius ke Fahreinheit===")

#No 5 mencari Luas dan Keliling Tabung
#input
jarijari,tinggi,volume,kelilingTabung,luasTabung="phi*r2","v/(phi*r2)","phi r2 t","2phi r","2phi r(r+t)"
print("Jari-Jari Tabung adalah", jarijari)
print("Tinggi Tabung adalah", tinggi)
print("Volume Tabung adalah", volume)
print("Keliling Tabung adalah", kelilingTabung)
print("luas Tabung adalah", luasTabung)