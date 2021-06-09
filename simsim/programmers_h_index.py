def solution(citations):
    answer = 0
    citations_max = max(citations)

    for i in range(1, citations_max):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i :
                cnt +=1
        if cnt == i :
            answer+=cnt

    return answer



print(solution([15,16,17,18]))