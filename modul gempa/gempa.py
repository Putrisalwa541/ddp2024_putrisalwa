class Gempa:
    lokasi = ' '
    skala = ' '
    
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        if self.skala <2 :
            ket = "Gempa Tidak Berasa"
        elif self.skala > 2  and self.skala <4:
            ket = "Bangunan Retak-Retak"
        elif self.skala >=4 and self.skala <6:
            ket = "Bangunan Roboh"
        else : 
            ket ="Bangunan Roboh dan Berdampak Tsunami"
                
        print("Lokasi Gempa", self.lokasi, "\nSkala Gempa", self.skala, "\nDampak Gempa",ket)
            