import sys
import time


def solution(arr):
    global overlap
    for i in range(len(arr)):
        rst = 0
        for j in range(i+1,len(arr)):
            if input_list[i] == 0:
                continue
            if input_list[i] == input_list[j]:
                rst += 1
                input_list[j] = 0
            else:
                continue
        if rst != 0:
            overlap.append(rst + 1)
        else:
            continue
    if len(overlap) == 0:
        overlap.append(-1)


overlap = []
input_list = list(map(int,sys.stdin.readline().split()))
s_t = time.time()
solution(input_list)
e_t = time.time()

print("time : ", e_t - s_t)



print(overlap)
