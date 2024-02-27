umur = int(input("Masukan umur anda :"))

if umur <=2 :
    print(" Panggilan anda adalah bayi" )
elif umur <=5 :
    print("Panggilan anda adalah balita" )
elif umur <=12 :
    print("Panggilan anda adalah anak - anak" )
elif umur <=17 :
    print("Panggilan anda adalah remaja" )
elif umur > 17 :
    print("Panggilan anda adalah dewasa" )
else:
    print("Panggilan anda adalah orang tua", umur > 30)