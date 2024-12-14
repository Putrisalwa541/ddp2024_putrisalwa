##super() untuk memanggil si filenya/ person nya, properti itu variabel
class Animal :
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
        print("Nama \t\t\t :", self.nama,
              "\nHidup \t\t\t :", self.hidup , 
              "\nMakanan \t\t :",self.makanan, 
              "\nBerkembangbiak \t\t :", self.berkembang_biak)
        
        
# binatang = Animal("kucing","ikan","darat","beranak")
# binatang.info_animal()