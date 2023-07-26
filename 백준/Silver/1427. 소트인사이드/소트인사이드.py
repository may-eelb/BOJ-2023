from sys import stdin
input = stdin.readline

N = input().strip()


number_list = [int(digit) for digit in N]
number_list.sort(reverse=True)

for i in number_list:
    print(i, end ="")