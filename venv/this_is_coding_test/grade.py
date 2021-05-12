import sys

#data = sys.stdin.readline().rstrip()
#print(type(data))
#print(data)

a = 10

def func() :
    global a
    a+=1
    print(a)

func()


b = [9,1,8,4]
c = sorted([9,1,8,5])
print(c)
