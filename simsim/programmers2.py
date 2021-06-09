import time

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr[:]:
        for j in arr[1:]:
            if i == j:
                del arr[i]
    answer.extend(arr)
    return answer


start_time = time.time()
print(solution([1,1,3,3,0,1,1]))
end_time = time.time()

print(end_time - start_time)

