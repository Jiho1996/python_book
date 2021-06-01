alist = [4, 5, 6, 11, 13, 15, 17, 21, 26, 28]

sum=0

sum += [num for num in alist if num % 3 == 0]

print(sum)