import sys

str_sentence=[]
str_sentence = list(map(str,sys.stdin.readline().rstrip().split(" ")))

finding_word = sys.stdin.readline().rstrip()

print(str_sentence)

for i in range(len(str_sentence)):
    if finding_word == str_sentence[i]:
        print("찾고싶은 단어위치 : "  , i+1)
    else : continue

