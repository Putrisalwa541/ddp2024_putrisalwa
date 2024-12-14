from Animal import *
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_sisik, bentuk_tubuh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_sisik = warna_sisik
        self.bentuk_tubuh = bentuk_tubuh
        
    def info_ikan (self) :
            super().info_animal(),
            print("Warna Sisik \t\t :", self.warna_sisik,
            "\nBentuk Tubuh \t\t :",self.bentuk_tubuh)
            
ikan_mas = Ikan("Mas", "Cacing","Air Tawar","Bertelur","Kuning Keemasan","Memanjang dan Memipih Tegak")
ikan_mas.info_ikan()
print("==============================================================================================")
ikan_nila = Ikan("Nila", "Cacing", "Air Tawar", "Bertelur", "Putih atau Merah", "Pipih, Memanjang dan Ramping")
ikan_nila.info_ikan()