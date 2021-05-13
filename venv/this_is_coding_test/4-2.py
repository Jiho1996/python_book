import sys




N = int(sys.stdin.readline().rstrip())

rst = 0
for i in range(N+1) :
    for j in range(60):
        for k in range(60):
            print(str(i) + str(j) + str(k))
            if '3' in str(i) + str(j) + str(k) :
                rst+=1



print(rst)