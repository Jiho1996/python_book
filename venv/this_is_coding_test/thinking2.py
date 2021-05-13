import sys

num = list(map(int,sys.stdin.readline().split()))

plus = 0
minus = 0

for i in range(0,10):
    if num[i] > 0 :
        plus += num[i]
    else :
        minus += num[i]

print(plus,"  ",minus)
#print(num)