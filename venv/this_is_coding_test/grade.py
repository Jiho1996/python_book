num = int(input("몇명 ?"))

grade = input("점수: ").split(" ")

for i in range(num):
    grade[i] = int(grade[i])

grade.sort(reverse=True)
print(grade)