from Animal import Animal
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, ekor):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.ekor = ekor
        
    def info_Ular (self):
            super().info_animal(),
            print("Berbisa \t\t :",self.berbisa, "\nEkor \t\t\t :",self.ekor)
            
ular_pandan = Ular ("Ular Pandan","Tikus atau Katak","di Tempat yang Lembab atau bersembunyi di bawah dedaunan","Bertelur","Tidak Berbisa","panjang, meruncing, dan ramping")
ular_pandan.info_Ular()
print("==================================================================================================================")
ular_sanca = Ular ("Ular Sanca","Tikus atau Ayam","Rawa dan Daerah Berair","Bertelur","Tidak Berbisa","ekor Pendek dan Tumpul")
ular_sanca.info_Ular()