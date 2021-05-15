import sys
import time
import operator

knight = list(map(str,sys.stdin.readline().rstrip()))


start_time = time.time()
knight[0] = ord(knight[0])
knight[1] = int(knight[1])

rst = 0

move =[ [2,-1], [2,1], [-2,1],[-2,-1],[1,-2],[-1,-2],[1,2],[-1,2] ]
for i in move:
    ans = list(map(operator.add,i,knight))
    if ans[0] < 97 or ans[0] > 104 :
        continue
    elif ans[1] <1 or ans[1] > 8 :
        continue
    else :
        rst+=1
print(rst)


end_time = time.time()

print("time : ", end_time-start_time)