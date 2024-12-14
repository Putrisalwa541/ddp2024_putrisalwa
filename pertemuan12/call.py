from Mahasiswa import *
from Dosen import * #ciptakan object

m1 = Mahasiswa('Rina','Wanita',20,'SI',3)
m1.cetak()
m2 = Mahasiswa('Salman','Pria',20,'TI',5)
d1 = Dosen('Rizky','Pria',39,'S.Si, M.Kom', 'LPPM')
d2 = Dosen('Nabil','Pria',32,'S.Si, M.Kom', 'LTSI')#gunakan fungsi2 yg ada di class 

d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()