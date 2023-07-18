
import sys

N = int(sys.stdin.readline())
my_list = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    my_list.append(temp)

sorted_list = sorted(my_list, key=lambda coord: (coord[1], coord[0]))

for numbers in sorted_list:
    print(f'{numbers[0]} {numbers[1]}')