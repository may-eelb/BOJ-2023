from sys import stdin
input = stdin.readline

def fx(n):
    ans = 1
    i = 1
    while True:
        if ans % N == 0:
            break
        ans += 10 ** i
        i += 1

    print(i)

while True:
    try:
        N = int(input().strip())
    except:
        break
    fx(N)

