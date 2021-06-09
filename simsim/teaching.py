score = []

num = int(input("Input the number of score : "))

for i in range(num):
    pt = int(input("Input score [%d/%d] : " %(i+1, num)))
    score.append(pt)

    print(score)
print("Average score is %.2f" %(sum(score)/len(score)))


