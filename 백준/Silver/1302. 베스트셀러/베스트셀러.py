from sys import stdin
input = stdin.readline

n = int(input())
my_dic = {}
for i in range(n):
    temp = input().strip()
    if temp in my_dic:
        my_dic[temp] += 1
    else :
        my_dic[temp] = 1


maxv = max(my_dic.values())
temps = [key for key, value in my_dic.items() if value == maxv]
sort_list = sorted(temps)
print(sort_list[0], sep = '\n')


