
N = int(input())
my_list = []

for i in range(N):
    my_list.append(list(map(int, input().split())))

my_list.sort()

for j in range(N):
    print(f'{my_list[j][0]} {my_list[j][1]}')