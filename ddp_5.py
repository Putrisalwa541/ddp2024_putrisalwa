kendaraan=["beat", "motor", 200, "pink", 3]
print(kendaraan)

kendaraan.append("10jt")
print(kendaraan)

kendaraan.append("matic")
print(kendaraan)

kendaraan.insert(2, "honda")
print(kendaraan)


#bangun datar
angka_pilihan=int(input("""Daftar menghitung luas bangun datar
1. menghitung luas persegi
2. mengitung luas lingkaran
3. menghitung luas segitiga
masukan pilihan:"""))

match angka_pilihan:
    case 1:
        print("menghitung luas persegi")
        sisi = int(input("masukan nilai sisi"))
        luas_persegi = sisi ** 2
        print(f"luas persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2")
        
    case 2:   
        print("menghitung luas lingkaran")
        phi=3.14
        jarijari= int(input("masukan nilai jarijari"))
        luas_lingkaran=phi*jarijari**2
        print(f"luas lingkaran dengan jari-jari {jarijari }cm, adalah {luas_lingkaran} cm")
        
    case 3:
        print("menghitung luas segitiga")
        tinggi =int(input("masukan nilai tinggi"))
        alas=int(input("masukan nilai alas"))
        luas_segitiga=1/2*tinggi*alas
        print(f"luas segitiga dengan tinggi {tinggi} cm dan alas {alas} cm, adalah {luas_segitiga} cm")
        
    case _:
        print("input tidak valid")