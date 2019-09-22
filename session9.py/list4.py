items = input("enter a list of number, separate by ' ': ").split(" ")
print(*items, sep=', ')
for i in items:
    if int(i) % 2 == 0:
        print("all even number in list: {}".format(i))