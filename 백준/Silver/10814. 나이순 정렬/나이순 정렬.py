
N = int(input())
my_list =[]

for i in range(N):
    temp = list(input().split())
    my_list.append(temp)

sorted_list = sorted(my_list, key=lambda x: int(x[0]))

for j in range(N):
    print(f'{sorted_list[j][0]} {sorted_list[j][1]}')