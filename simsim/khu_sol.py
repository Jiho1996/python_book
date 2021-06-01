A_list = [2.7, 'ace', 5, 12, 'white', 6.7, 12.8, 21, 41.9, 11, 22.3]
B_list = []


B_list = [num for num in A_list if type(num) == int]

print(B_list)