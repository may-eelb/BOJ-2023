from sys import stdin
input = stdin.readline



while (1):
    N = int(input())
    if N == 0:
        break
    re = []
    for i in range(N):
        temp = list(input().split())

        re.append(temp)
    for ttemp in re:
        ttemp[1] = float(ttemp[1])

    re.sort(key=lambda x: x[1], reverse=True)
    max = re[0][1]
    num = 0
    anw =[]
    for ttemp in re:
        if ( max == ttemp[1]):
            anw.append(ttemp[0])

    print(*anw)
