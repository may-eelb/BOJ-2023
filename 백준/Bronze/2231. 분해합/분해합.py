
n = int(input())
answer = 0


for i in range(1, n):
    mylist = []


    copy_i = i
    while copy_i != 0:
        temp = copy_i % 10
        mylist.append(temp)
        copy_i = copy_i // 10

    if i + sum(mylist) == n:
        answer = i
        break

print(answer)
