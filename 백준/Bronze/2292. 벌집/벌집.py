
N = int(input())
temp = 1
step = 0
i = 0



while ( temp + 6 * i <= N):
    temp = temp + 6 * i
    i = i + 1
    step = step+1


if N - temp > 0 :
    step += 1

print(step)