from sys import stdin
input = stdin.readline
from collections import deque
import copy

n, m = map(int, input().split())

target = list(map(int, input().split()))
my_list = [i for i in range(1, n + 1)]
my_deque = deque(my_list)
#print(my_deque)
cnt = 0

for temp in target:
    count2 = 0
    count3 = 0
    copy1 = copy.copy(my_deque)
    copy2 = copy.copy(my_deque)

    while True :
        if temp == copy1[0]:
            break
        copy1.rotate(-1)
        count2 += 1

    while True :
        if temp == copy2[0]:
            break
        copy2.rotate(1)
        count3 += 1

    #print(f'2 : {count2} 3 :{count3}')

    if count2 > count3 :
        cnt += count3
        my_deque.rotate(count3)
        my_deque.popleft()
    else:
        cnt += count2
        my_deque.rotate(-count2)
        my_deque.popleft()


print(cnt)
