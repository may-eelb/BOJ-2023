from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
my_list = list(map(int, input().split()))
sum_list = []
sum_list.append(0)
sum_list.append(my_list[0])

#print(sum_list)
for i in range(2,N+1):
    sum_list.append( sum_list[i-1] + my_list[i-1])
#print(sum_list)

for j in range(M):
    a , b = map(int, input().split())
    print(sum_list[b] - sum_list[a-1])