items = ['bong da', 'bong ro', 'lol', 'pubg']
new_hobby = input("mon moi: ")
items.append(new_hobby)
i = int(input("nhap so vao: "))
thaythe = input("nhap chu vao: ")
items[i] = thaythe
print(*items, sep=', ')