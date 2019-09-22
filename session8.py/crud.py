while True:
 items = ['c','r','u','d']
 print(*items, sep= ', ')
 otheritems = ['mcdonald','sumobbq','kingbbq', 'thai express']
 print(*otheritems, sep=', ')
 chooseone = input("hay chon 1 chu: ")
 if chooseone == 'c':
     favorite = input("hay them do ban muon: ")
     otheritems.append(favorite)
     print(*otheritems, sep=', ')
 elif chooseone == 'r':
     if len(otheritems) == 0:
        print("List rong")
     else:
         for i in range(len(otheritems)):
             print(otheritems[i])
 elif chooseone =='u':
     i = int(input("nhap so vao: "))
     thaythe = input("nhap chu vao: ")
     otheritems[i] = thaythe
     for i, otheritem in enumerate(otheritems):
         print(i + 1,',',otheritem.upper())
 elif chooseone == 'd':
     n = int(input("nhap so muon xoa vao: "))
     otheritems.pop(n)
     print(*otheritems, sep=', ')
 else:
     print("nhap sai roi. vui long nhap lai")

    
    
           