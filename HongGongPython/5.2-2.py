max_limit = 6
min_limit = 2
num = 6
memo = {}

def seat(remain, seating) :
    key = str([remain,seating])
    if key in memo :
        return memo[key]
    if remain < 0:
        return 0  # 무효하니 0을 리턴
    if remain == 0:
        return 1  # 유효하니 수를 세면 되서 1을 리턴
        # 재귀 처리
    count = 0
    for i in range(seating, max_limit + 1):
        count += seat(remain - i, i)
        # 메모화 처리
    memo[key] = count
        # 종료
    return count

print(seat(6,min_limit))