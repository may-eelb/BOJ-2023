
N, M = map(int, input().split())

my_list = list(map(int, input().split()))

x = M
answer = 0

for i in range(N-2):
    for j in range( i + 1 , N-1):
        for k in range( j +  1, N):
            temp = my_list[i] + my_list[j] + my_list[k]
            if M-temp >= 0 and M - temp <= x:
                x = M - temp
                answer = temp

print(answer)
