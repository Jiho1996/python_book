import sys

def fact(n):
    if n >1:
        return n * fact(n-1)
    else :
        return 1

print("수를 입력하시오. : ", end=' ')
num = int(sys.stdin.readline().rstrip())
rst = 1

for i in range(1,num+1) :
    rst  = rst*i

print(rst)
print(fact(5))


