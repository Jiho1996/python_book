import sys
import time


N , K = map(int, sys.stdin.readline().split())

start_time = time.time()
rst = 0

while(True):
    if N == 1 :
        break
    else :
        if N % K == 0 :
            N = N // K
            rst +=1
        else :
            N -= 1
            rst +=1
print(rst)

end_time = time.time()
print("time: " , end_time - start_time)

