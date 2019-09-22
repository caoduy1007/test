#sothich = input("name your thing: ")
#hobby = sothich.split(',')
#print = ("your thing:")
#for i in range(len(hobby)):
#    print(hobby[i])

#from random import shuffle
#mottu = input("enter a word: ")
#nhaychu = list(mottu)
#shuffle(nhaychu)
#print("jumbled word:")
#for i in range(len(nhaychu)):
#    print(nhaychu[i])


from random import randint
from random import shuffle
items = ['planet', 'champion','earthquake','tsunami']
i = randint(0,3)
mottu = items[i]
nhaychu = list(mottu)
shuffle(nhaychu)
print("jumbled word:")
for i in range(len(nhaychu)):
    print(nhaychu[i])
answer = input("hay nhap cau tra loi vao: ")
if mottu == 'planet':
    if answer == 'planet':
        print('dung roi')
    else:
        print('sai roi')
if mottu == 'champion':
    if answer == 'champion':
        print('dung roi')
    else:
        print('sai roi')
if mottu == 'earthquake':
    if answer == 'earthquake':
        print('dung roi')
    else:
        print('sai roi')
if mottu == 'tsunami':
    if answer == 'tsunami':
        print('dung roi')
    else:
        print('sai roi')
   