print("Quan", "Dan so quan (nguoi)","Dien tich (km2)","mat do dan so (nguoi/km2)", sep='/ ')
items = ['Ba Dinh', 'Cau Giay', 'Hai Ba Trung', 'Son Tay', 'Bac Tu Liem', 'Dong Da']
items2 = [247100, 266800 , 318000, 150300, 333300, 420900]
items3 = [32.27, 12.04, 9.62 ,113.5 ,43.35 ,9.96]
listZIp = list(zip(items, items2, items3))
listZIp2 = list(zip(items, items2, items3, items4))
for j in range(len(listZIp2)):
    print(*listZIp2[j])
for i in range(len(listZIp2)):
    if max(items2) == listZIp2[i][1]:
       print("Quan co dan so lon nhat la:",listZIp2[i][0])
    if min(items2) == listZIp2[i][1]:
       print("Quan co dan so nho nhat la:",listZIp2[i][0])
  