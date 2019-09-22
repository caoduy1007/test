#items = ['bong da', 'lol', 'pubg', "twice"] 
#print(*items, sep=', ')
#new_hobby = input("so thich khac: ")
#items.append(new_hobby)
#print(*items, sep=', ' ) 


items = ['bong da', 'lol', 'pubg', "twice"] 
print(*items, sep='| ')
new_hobby = input("so thich khac: ")
items.append(new_hobby)
#print(items[0])
#print(items[4])
#print(items[3])
for i, item in enumerate(items):
 print(i + 1,'.', item)
[items.upper() for items in ["bong da","lol","pubg"," twice"]]