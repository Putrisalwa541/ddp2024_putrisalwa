#program menentukan bilangan ganjil dan genap
print('## 1. program bilangan ganjil dan genap ##')
print()

#input bilangan
bilangan= int(input("masukan bilangan anda :"))
if bilangan % 2 == 0 :
  print(bilangan, "merupakan bilangan genap")
else:
    print(bilangan,"merupakan bilangan ganjil")
   
    
 #program menentukan nilai
print('## 2.menentukan nilai ujian ##')
print()
 
  #input nilai ujian
nilai_ujian = int(input("masukan nilai anda :"))
if nilai_ujian >= 75:
  print("kamu dinyatakan lulus")
else:
  print("kamu dinyatakan tidak lulus")
  
('## 3.menentukan usia ##')
print()

#input usia
usia=int(input("masukan usia anda:"))
if usia >=18:
    print("kamu dewasa")
elif usia >=13 and usia <=17:
    print=("kamu remaja")
else:
    print("kamu anak-anak ")
    
('## 4. menentukan keanggotaan ##')
print()
    
 #input status
status_anggota = input('''Daftar Keanggotaan Dibawah ini
                        1.gold
                        2.silver
                        3.bronze
                        masukan pilihan kamu:''')
if status_anggota=='gold' or status_anggota== 'silver':
    print("selamat anda mendapatkan diskon")
elif status_anggota=='bronze':
    print("maaf anda tidak mendapatkan diskon")
else:
    print("masukan kata dengan benar")
     
    
('## 5. jumlah pembelian ##')
print()

#input pembelian diskon
minyak = 16.000
telur = 30.000
beras = 50.000
sembako = 100.000
jumlah=(minyak + telur + beras + sembako)
print(f"total={jumlah}")
jumlah_pembelian=int(input("masukan jumlah pembelian:"))
if jumlah_pembelian >=100:
  print("mendapatkan diskon 10%")
else:
  print("tidak mendapatkan diskon")
 