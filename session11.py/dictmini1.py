computer = {
    'HP': '20',
    'DELL': '50',
    'MACBOOK': '12',
    'ASUS': '30',
}
for k, v in computer.items():
    print(k, v, sep= ': ')
computer['TOSHIBA'] = '10'
print(computer)
tim_kiem = input("may can tim kiem: ")
if tim_kiem in computer.keys(): 
     print("so may trong kho la:",computer[tim_kiem] )