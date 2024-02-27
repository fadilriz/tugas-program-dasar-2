english =int(input(" masukan nilai anda english:"))
mtk =int (input(" Masukan nilai mtk :"))
ipa =int (input(" masukan nilai ipa :"))
ips =int (input(" masukan nilai ips :"))
indo =int (input(" masukan nilai indo :"))

rata_rata = ( english + mtk + indo ) / 3
rata_rata_semua = (english +mtk +ipa + ips + indo) / 5

if rata_rata >= 75 :
    print (" dia lulus ")
elif rata_rata_semua >= 70:
    print(" maka dia lulus ")
elif mtk > 90 and english > 90:
    print(" maka dia lulus ")
else:
    print(" maka dia tidak lulus ")
