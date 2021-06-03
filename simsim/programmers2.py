def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    d_count = 0
    z=0
    for i in range(len(arr)-1):
        for j in range(i+1,i+2):
            if arr[i] == arr[j] :
                arr[i] = -100

    d_count = arr.count(-100)

    for _ in range(len(arr)):

        if arr[z] == -100:
            del arr[z]
        else :
            answer.append(arr[z])
            z = z + 1


    return answer


print(solution([1,1,3,3,0,1,1]))