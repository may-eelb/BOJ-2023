from sys import stdin
input = stdin.readline

my_list = list(input().strip())

N = int(input())
right = []
for i in range(N):
    temp = list(input().split())

    if len(temp) > 1 :
        my_list.append(temp[1])

    else:
        if temp[0] == "L":
            if my_list:
                right.append(my_list.pop())
        elif temp[0] == "D":
            if right:
                my_list.append(right.pop())
        else:
            if my_list:
                my_list.pop()




print(*(my_list + right[::-1]), sep ="")

