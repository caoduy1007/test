items = input("enter a list of number, separate by ' ': ").split(" ")
print(*items, sep=', ')
pop = 0
for i in items:
    pop = pop + int(i)
print("sum of all number:",pop)
#n = int(input("enter a number:"))
# for i in range(len(items)):
#     if n == items[i]:
#         print("found, position {} : {}". format(i, items[i] ))
#if n in items:
#    print("found, position {} : {}". format(items.index(n), n))
#else:
#    print("not found in our list")
#a = sum(items)
#print("sum of all number:", a)
