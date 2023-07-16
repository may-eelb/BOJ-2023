
N = int(input())

answer = []
cnt = 0
i = 0
while (cnt < N ):

    temp = str(i)
    if "666" in temp:
        cnt += 1
        answer.append(i)
    i += 1

print(answer[N-1])
