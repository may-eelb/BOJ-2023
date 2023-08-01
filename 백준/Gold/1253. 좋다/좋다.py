from sys import stdin
input = stdin.readline



n = int(input())
my_list = list(map(int, input().split()))


my_list.sort()
count = 0
for idx in range(n):
    target = my_list[idx]
    i = 0
    j = n - 1


    while i < j:
        if my_list[i] + my_list[j] == target:
            if i != idx and j != idx :
                count+= 1
                break
            elif i == idx:
                i += 1
            elif j == idx:
                j -= 1
        elif my_list[i] + my_list[j] > target:
            j -= 1
        elif my_list[i] + my_list[j] < target:
            i += 1

print(count)