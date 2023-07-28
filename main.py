faktoriyel = 1

while True:
    sayi = int(input("lütfen pozitif değer giriniz:"))
    if (sayi<=0):
        print("lütfen pozitif bir değer giriniz.")
    else:
        for i in range(1,sayi+1):
            faktoriyel = faktoriyel*i
        print("faktoriyel",faktoriyel)
        break
