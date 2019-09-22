names = ['bong ro', 'bong da', 'lol', "abcO"]
new_hobby = input("nhap chu vao: ")
names.append(new_hobby)
for i, name in enumerate (names):
    if ("o" in name) or ("O" in name):
        print(i + 1,'.', name.upper())

