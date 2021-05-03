# *매개변수 == 매개변수가 몇개인지 모를때
def mul(*value):
    rst = 1
    for i in value:
        rst = rst * i
    return rst

print(mul(5,7,9,10))
