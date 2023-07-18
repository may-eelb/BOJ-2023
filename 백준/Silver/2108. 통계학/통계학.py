from sys import stdin
input = stdin.readline

from collections import deque
from collections import Counter

N = int(input())
my_list = deque()
for i in range(N):
    my_list.append(int(input()))

my_list = sorted(my_list)

#산술평균
print(round(sum(my_list)/len(my_list)))

#중앙값
print(my_list[int((N-1)/2)])

#최빈값
counter = Counter(my_list)
max_idx = []
answer = 0
max_count = max(counter.values())
max_idx = [value for value, count in counter.items() if count == max_count]
if len(max_idx) > 1:
    print(max_idx[1])
else:
    print(max_idx[0])


if N == 1:
    print(0)
else:
    print(abs(my_list[-1] - my_list[0]))