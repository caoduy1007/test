n = int(input("hay nhap thang ban muon : "))
if n == 2:
    print("thang nay co 28 hoac 29 ngay")
elif n in (1, 3 ,5, 7, 8, 10, 12):
    print("thang nay co 31 ngay")
elif n in (4, 6, 9, 11):
    print("thang nay co 30 ngay")
else:
    print("chi co tu thang 1 den thang 12 thoi")

