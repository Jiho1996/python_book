num = int(input("몇명 ?"))

grade = list(map(int,input().split(" ")))


grade.sort(reverse=True)
print(grade)