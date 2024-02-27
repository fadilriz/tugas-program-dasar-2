masukan_tahun = int(input("Masukan tahun :"))

if masukan_tahun %4 == 0 :
    print("%i Adalah tahun kabisat " % masukan_tahun)
else:
    print("%i Bukan tahun kabisat " % masukan_tahun)