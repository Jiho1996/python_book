character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃 검",
        "armor" : "소울블레이드"},
    "skill" : ["베기", "물기", "꼬집기"]
}

print(character["skill"][0])

#for key in character:
#    if type(character[key]) != dict and type(character[key]) != list:
#        print(key ,":",character[key])

#    elif type(character[key]) is dict:

#        for smallkey in character[key] :

#            print(key,":", character["items"][smallkey])


#    elif type(character[key]) is list :

#        for i in range(3) :
#            print(key, ":", character["skill"][i])


