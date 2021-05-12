import sys
import time


N, M, K = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
start_time = time.time()
rst = 0
num.sort(reverse=True)
gap = num[0] - num[1]
turn = M // K
rst += num[0]*M - gap*turn


print(rst)
end_time = time.time()
print("time:", end_time-start_time)