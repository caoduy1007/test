price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000
}
for k, v in price.items():
    print(k, v, sep= ': ')
checkgia = input("chon mot may tinh: ")
if checkgia in price.keys():
    print("gia tien cua 1 may la: ",price[checkgia])
number = int(input("so luong may mua la: "))
a = number * price[checkgia]
print("TONG GIA TRI HOA DON LA:",a)
price[checkgia] -= number
for k, v in price.items():
    print(k, v, sep= ': ' )