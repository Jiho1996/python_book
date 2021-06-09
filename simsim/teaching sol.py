import sys

input_list = list(map(int, sys.stdin.readline().split()))
rst = sum(input_list)/len(input_list)
print(rst)