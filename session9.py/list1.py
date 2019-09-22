items = ['blue', 'red',' teal','green']
print("Our list: ")
print(*items, sep=', ')
new_color = input("enter new color: ")
items.append(new_color)
print("Our new color list: ")
print(*items, sep=', ')

