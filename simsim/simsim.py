import sys
import time
import math

B, N = map(int , sys.stdin.readline().split())
start_time = time.time()

rst_list = []
rst =[]

for A in range(1,1000001):
    rst = B - A**N
    rst = abs(rst)

    rst_list.append([rst,A])

rst_list.sort()
print(rst_list[0][1])
end_time = time.time()

print("시간:",end_time-start_time)


p = pow(B,1/N)
a = round(p,0)
print("두번째답:",int(a))