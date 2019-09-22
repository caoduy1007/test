from random import randint
points = 0
while True:
    num1 = randint(1, 30)
    num2 = randint(1, 30)
    resultFalse = randint(-3, 3)
    result = num1 + num2 + resultFalse
    print(num1, "+" , num2, "=", result)
    answer = input("Yes or No ? ").lower()
    if resultFalse == 0 :
        if answer == "yes":
            points += 1
            print("points",points)
        if answer == "no":
            print("SAI ME M ROI. GAME OVER")
            break
    if resultFalse != 0 :
        if answer == "no":
            points += 1
            print("points",points)
        if answer == "yes":
            print("SAI ME M ROI. GAME OVER")
            break
         
        
