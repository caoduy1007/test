items =['bong da', 'bong ro', 'lol', 'pubg']
items.pop(0)
if "lol" in items:
    items.remove('lol')
else:
    print("not in list")
print(*items, sep=', ')