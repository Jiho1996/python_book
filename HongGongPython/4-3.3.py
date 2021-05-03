limit = 10000
sum_value = 0
a= 1
while True :
    sum_value = sum_value + a
    if sum_value < limit:
        print(a,"+", end= " ")
        a = a+1
        continue
    else :
        print(a, "=\n", sum_value)
        print("{} 이거닷!".format(a))
        break



