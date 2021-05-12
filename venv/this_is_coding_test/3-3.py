import sys
import time
import random

M, N = map(int, sys.stdin.readline().split())

rst = []

for _ in range(M) :
    card_list = list(map(int,sys.stdin.readline().split()))
    rst.append(min(card_list))
    print(rst)


print(max(rst))

