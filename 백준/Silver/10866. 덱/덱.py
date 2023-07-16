
import sys
from collections import deque

my_deque = deque()
N = int(sys.stdin.readline())

for i in range(N):
    temp = list(sys.stdin.readline().split())
    if (temp[0] == "push_front"):
        my_deque.appendleft(temp[1])

    elif (temp[0] == "push_back"):
        my_deque.append(temp[1])

    elif (temp[0] == "pop_front"):
        if my_deque:
            print(my_deque[0])
            my_deque.popleft()
        else:
            print(-1)

    elif (temp[0] == "pop_back"):
        if my_deque:
            print(my_deque[-1])
            my_deque.pop()
        else:
            print(-1)

    elif (temp[0] == "size"):
        print(len(my_deque))

    elif (temp[0] == "empty"):
        if my_deque:
            print(0)
        else:
            print(1)
    elif (temp[0] == "front"):
        if my_deque:
            print(my_deque[0])
        else:
            print(-1)
    elif (temp[0] == "back"):
        if my_deque:
            print(my_deque[-1])
        else:
            print(-1)