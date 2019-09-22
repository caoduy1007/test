from turtle import *

canh = int(input("Nhap canh ban muon ? "))
polygon = 360 / canh

for i in range(canh):
    forward(100)
    left(polygon)

mainloop()