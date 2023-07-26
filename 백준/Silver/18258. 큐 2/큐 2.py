from collections import deque
import sys
queue = deque()

N = int(sys.stdin.readline())
for i in range(N):
    temp = list(sys.stdin.readline().split())
    if (len(temp) == 2):  ## push
        queue.append(temp[1])

    elif temp[0] == "pop":
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.popleft())


    elif temp[0] == "size":
        print(len(queue))
    elif temp[0] == "empty":
        if (len(queue)) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == "front":
        if (len(queue)) != 0:
            print(queue[0])
        else :
            print(-1)
    else:
        if (len(queue)) != 0:
            print(queue[-1])
        else :
            print(-1)