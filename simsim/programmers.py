def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_ans =[]
    second_ans =[]
    third_ans = []

    first_rst = 0
    second_rst = 0
    third_rst = 0

    answers_len = len(answers)
    for _ in range(2001):
        first.extend(first)
    for _ in range(1251):
        second.extend(second)
    for _ in range(1001):
        third.extend(third)
    for i in range(answers_len):
        first_ans.append(first[i])
        second_ans.append(second[i])
        third_ans.append(third[i])
    for i in range(answers_len) :
        if first_ans[i] == answers[i] :
            first_rst+=1
        if second_ans[i] == answers[i]:
            second_rst+=1
        if third_ans[i] == answers[i] :
            third_rst+=1

        else : continue

    rst_list =[]

    rst_list.extend([first_rst,second_rst,third_rst])
    print(rst_list)





answers = [1,2,3]
solution(answers)