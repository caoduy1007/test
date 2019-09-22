print("high score:")
score = [56, 45, 67, 78]
while True:
    count = 0
    reverseList = sorted(score, reverse=True)
    for i, item in enumerate(reverseList):
        count += 1
        if count < 6:
            print(i + 1,',', item)
    j = int(input("enter your new high score: "))
    score.append(j)
    