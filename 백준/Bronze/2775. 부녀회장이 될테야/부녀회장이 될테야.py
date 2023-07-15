

my_list = []
for i in range(15):
    my_list.append([0] * 14)
my_list[0] = [1, 2, 3,4,5,6,7,8,9,10, 11,12,13,14]


for j in range(1, 15):
    for k in range(0, 14):
        sum = 0
        for t in range(k+1):
            sum += my_list[j-1][t]
        my_list[j][k] += sum

N = int(input())

for n in range(N):
    층 = int(input())
    호 = int(input())

    print(my_list[층][호-1])

