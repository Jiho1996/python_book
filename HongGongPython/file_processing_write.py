import random
hanguls = list("가나다라마바사아자차카타파하")
with open("basic.txt","w") as file:
    for i in range(100):
        name = random.choice(hanguls) + random.choice(hanguls)
        age = random.randrange(1,100)
        height = random.randrange(150,200)
        weight = random.randrange(40,100)
        file.write("{},{},{},{}\n".format(name,age,height,weight))