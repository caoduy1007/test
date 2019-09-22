while True:
 count = 0
 print("How many legs does an pctopus have?")
 answer = {
    '1': 'four legs',
    '2': 'two legs',
    '3': 'eight legs',
    '4': 'no legs'
 }
 for k, v in answer.items():
     print(k, v, sep='.')
 i = int(input("what is your answer? "))
 if i == 3:
     count += 1
     print("score:", count)
 else:
     print("score", count)
