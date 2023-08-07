from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
my_list = list(input().strip())

temp = []
cnt = 0


for c in my_list:

    int_c = int(c)
    while temp and cnt < m and temp[-1] < int_c:
        temp.pop()
        cnt += 1
    #print(f'이번에 넣는 숫자 : {int_c}')
    if len(temp) < n - m:
        temp.append(int_c)


print(*temp, sep = "")

