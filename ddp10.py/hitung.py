import math

def tambah(bil1,bil2):
    hitung = (bil1+bil2)
    print(f"Hasil Tambah dari", bil1, "+" ,bil2 ,"=" ,hitung)
    
def kurang(bil1,bil2):
    hitung = (bil1-bil2)
    print(f"Hasil Kurang dari", bil1, "-" ,bil2 ,"=" ,hitung)
    
def kali(bil1,bil2):
    hitung = (bil1*bil2)
    print(f"Hasil Kali dari", bil1, "*" ,bil2 ,"=" ,hitung)
    
def bagi(bil1,bil2):
    hitung = (bil1/bil2)
    print(f"Hasil Bagi dari", bil1, "/" ,bil2 ,"=" ,hitung)
    
def pangkat(bil1,bil2):
    hitung = math.pow(bil1,bil2)
    print(f"Hasil Pangkat dari", bil1, "^" ,bil2 ,"=" ,hitung)