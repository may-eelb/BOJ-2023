from sys import stdin
input = stdin.readline
import re
from collections import deque

T = int(input())
for _ in range(T):
    command = list(input().strip())
    #print(command)
    n = int(input())
    temp = input()
    ml = [int(num) for num in re.findall(r'\d+', temp)]
    my_deque = deque(ml)
    error = False

    Rcount = 0
    for c in command:
        #print(c)
        if c == "D":
            if my_deque:
                if Rcount % 2 == 0:
                    my_deque.popleft()
                else:
                    my_deque.pop()
            else:
                error = True
        else:
            Rcount += 1

    if Rcount % 2 != 0:
        my_deque.reverse()

    if error:
        print("error")
    else:
        if my_deque:
            print('[', end ="")
            print(*my_deque, sep =",", end ="")
            print(']')
        else:
            print("[]")

