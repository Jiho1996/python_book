def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    first_rst = 0
    second_rst = 0
    third_rst = 0

    if len(answers) > len(first) or len(answers) > len(second) or len(answers) > len(third):
        f = len(answers) - len(first)
        s = len(answers) - len(second)
        t = len(answers) - len(third)
        if f > 0 :
            if f > 5 :
                f_h = f // 5
                f_n = f % 5
                first.extend(first * f_h)
                first.extend(first[:f_n])
            else : first.extend(first[:f])
        if s > 0 :
            if s > 8 :
                s_h = s//8
                s_n = s % 8
                second.extend(second * s_h)
                second.extend(second[:s_n])
            else : second.extend(second[:f])
        if t > 0 :
            if t > 10 :
                s_h = s//10
                s_n = s % 10
                third.extend(third * s_h)
                third.extend(third[:s_n])
            else : third.extend(third[:f])

        for i in range(len(answers)):
            if answers[i] == first[i]:
                first_rst += 1
            if answers[i] == second[i]:
                second_rst += 1
            if answers[i] == third[i]:
                third_rst += 1
    else :
        for i in range(len(answers)):
            if answers[i] == first[i]:
                first_rst += 1
            if answers[i] == second[i]:
                second_rst += 1
            if answers[i] == third[i]:
                third_rst += 1

    cal = [first_rst,second_rst,third_rst]
    cal.sort(reverse=True)

    if first_rst == second_rst == third_rst :
        answer.extend([1,2,3])

    elif cal[0] == first_rst:
        answer.append(1)
    elif cal[0] == second_rst:
        answer.append(2)
    elif cal[0] == third_rst:
        answer.append(3)

    return answer


print(solution([2,1,2,3,4]))