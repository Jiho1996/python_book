a= [1, 5, 3, 20, 18, 9, 7, 22, 33, 10]

for i in range(len(a)) :
    if i == 9 :
        a[-1] = a[0]
    else :
        a[i] = a[i+1]
        i+=1

print(a)