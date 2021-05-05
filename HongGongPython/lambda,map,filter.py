def power(item):
    return item*item
def under_3(item):
    return item<3

list_input_a = [1,2,3,4,5]

output = map(lambda x : x*x,list_input_a)
print(list(output))
output2 = filter(lambda x:x<3,list_input_a)
print(list(output2))