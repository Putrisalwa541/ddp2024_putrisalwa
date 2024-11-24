#nomor 1
def celcius_ke_farenheit(celcius):
    hasil_perhitungan = (celcius * 9/5 ) + 32
    return hasil_perhitungan
    
print(celcius_ke_farenheit(0))
print(celcius_ke_farenheit(100))

#nomor 2
def is_genap(angka):
    return angka %2 == 0

print(is_genap(4))
print(is_genap(7))

#nomor 3
def nilai_ujian(lulus):
 if lulus >= 75:
     return 'lulus'
 else:
    return 'tidak lulus'
print(nilai_ujian(100))
print(nilai_ujian(60))


#nomor 4
def bilangan_ganjil(nilai):
    for i in range(1, nilai ,2):
        print(i, end=" ")
        
bilangan_ganjil(20)
print()
    
    
#ini tantangan kalo bisa pulang
def ddp(ketentuan):
    if ketentuan== "bisa":
        print("syamil pulang")
    elif ketentuan== "ga bisa":
        print("syamil gabisa pulang")
    else:
        print("inputan tidak valid")
ddp("bisa")