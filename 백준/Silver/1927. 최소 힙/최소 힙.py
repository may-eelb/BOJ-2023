from sys import stdin
input = stdin.readline
import heapq

N = int(input())
O = [int(input()) for _ in range(N)]
min_heap = []
result = []
for x in O:
    if x > 0:
        heapq.heappush(min_heap, x)
    else:
        if not min_heap:
            result.append(0)
        else:
            smallest = heapq.heappop(min_heap)
            result.append(smallest)

for value in result:
    print(value)
