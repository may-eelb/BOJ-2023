N = int(input())

temp = []
num = 1
answer = ""
result = True

for i in range(N):
    target = int(input())
    if ( target >= num ):       # 무조건 출력가능
        while (target >= num):
            temp.append(num)
            num += 1
            answer += "+\n"
        temp.pop()
        answer += "-\n"

    else:  # pop만 해야하는 상황에서 애초부터 -1 애가 target보다 작으면 절대 못뽑는다
        if (temp[-1] < target):

            result = False
            break
        else:
            temp.pop()
            answer+= "-\n"

if (result):
    print(answer)

else:
    print("NO")
