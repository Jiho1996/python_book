def replace_set(def_list):
    for i in range(len(def_list)-1) :
        if def_list[i] == def_list[i+1]:
            def_list[i] = "x"

    #for i in range() :
        #if def_list[i] == "x" :
            #del def_list[i]
    for _ in range(def_list.count("x")):
        def_list.remove("x")
    return def_list

test_list = [1,2,2,3,3,4,4,1]

print(replace_set(test_list))


