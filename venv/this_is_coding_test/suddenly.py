arr = [[5,1],1,2,[3,[4]]]
d = []
def flatten(arr):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            flatten(arr[i])
        else :
            d.append(arr[i])
    return d

print(flatten(arr))


