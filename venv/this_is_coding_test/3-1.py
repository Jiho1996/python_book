import sys

N = int(sys.stdin.readline().rstrip())

coin = [ 500, 100, 50, 10 ]
rst = 0
for i in coin:
    rst = rst + (N // i)
    N = N - ((N // i)*i)
    # N %= i

print(rst)

