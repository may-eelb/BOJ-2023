

n = int(input())
my_list = []
for i in range(n):
    temp = int(input())
    my_list.append(temp)

my_list.sort()


for i in range(n):
    print(f'{my_list[i]}')