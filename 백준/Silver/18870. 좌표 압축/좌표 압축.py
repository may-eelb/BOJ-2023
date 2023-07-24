from sys import stdin
input = stdin.readline

N = int(input())
my_list = list(map(int, input().split()))

sorted_list = sorted(set(my_list))


count_dict = {}
for i in range(len(sorted_list)):
    count_dict[sorted_list[i]] = i

for k in my_list:
    print(count_dict[k], end = " ")