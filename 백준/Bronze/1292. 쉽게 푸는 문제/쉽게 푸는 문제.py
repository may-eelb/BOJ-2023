A , B = map(int, input().split())

my_list = []
for i in range(1, B+1):
    for j in range(1, i+1):
        my_list.append(i)

sum = 0
for k in range(A-1, B):
    sum += my_list[k]

print(sum)