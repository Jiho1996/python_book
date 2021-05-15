import sys

now = []

def move(a,b) :
    if b-1 > 0:
        b = b- 1
        return a , b
    else :
        pass

map_size = map(int, sys.stdin.readline().split())

x,y,place = map(int, sys.stdin.readline().split())

map_list = []
for  _ in range(4):
    map_list.append(list(map(int,sys.stdin.readline().split())))

move(x,y)
now = map_list[]


print(now)



