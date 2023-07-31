from sys import stdin
input = stdin.readline

my_list = list(input())

open = False
temp = []
answer =[]
for c in my_list:


    if c == "<":
        if temp:
            while temp:
                answer.append(temp.pop())
        answer.append(c)
        open = True
    elif c == ">":
        answer.append(c)
        open = False

    elif open == False and c == " " :
        if temp:
            while temp:
                answer.append(temp.pop())
        answer.append(c)

    elif open == False and c == "\n" :
        if temp:
            while temp:
                answer.append(temp.pop())


    elif open :
        answer.append(c)

    elif open == False :
        if c != " " or c != "<":
            temp.append(c)

print(*answer, sep ="")