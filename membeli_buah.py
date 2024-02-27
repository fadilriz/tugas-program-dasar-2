beli_buah = int(input("Berapa kilo buah yang anda beli :"))

if beli_buah <= 2 :
    print("Harganya adalah :", beli_buah * 20_000)
elif beli_buah > 2 and beli_buah <= 5 :
    print("Harganya adalah :", beli_buah * 18_000)
else:
    print("Harganya adalah :", beli_buah * 16_000)