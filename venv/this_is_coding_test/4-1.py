import sys
import time
N = int(sys.stdin.readline().rstrip())
move = list(map(str,sys.stdin.readline().split()))
start_time = time.time()

a, b = 1, 1

for i in move:
    if i == 'R':
        b += 1
        if b == 6:
            b -= 1
    elif i == 'L':
        b -= 1
        if b ==0:
            b += 1
    elif i == 'U':
        a -= 1
        if a == 0:
            a+=1
    elif i == 'D':
        a += 1
        if a == 6:
            a-=1
    else:
        print("잘못입력한 기호")

#for i in range(N):
#    for j in range(N):
#        square.append([i+1,j+1])

print(a ,b)
end_time = time.time()

print("time : " , end_time - start_time)