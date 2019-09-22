#print("our color list:")
#items = ['blue', 'green', 'red', 'teal']
#for i, item in enumerate(items):
#    print(i + 1,',',item.upper())
#delete = int(input("item to delete:"))
#items.pop(delete - 1)
#for i, item in enumerate(items):
#    print(i + 1,',',item.upper())


from turtle import *

items = ['blue', 'red', 'green', 'pink']
shape("turtle")
for i in range(len(items)):
    color(items[i])
    forward(100)
    right(90)
mainloop()