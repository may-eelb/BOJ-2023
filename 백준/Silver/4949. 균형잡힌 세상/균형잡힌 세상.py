from sys import stdin
input = stdin.readline

from collections import deque

while True:
    answer = "yes"
    my_str = input()
    deque1 = deque()
    deque2 = deque()


    if my_str == ".\n":
        break
    else:
        for c in my_str:
            if c == "(":
                deque1.append("(")

            elif c == "[":
                deque1.append("[")

            elif c == ")":
                if (len(deque1) == 0 or deque1[-1] == "["):
                    answer = "no"
                    break
                else:
                    deque1.pop()


            elif c == "]":
                if (len(deque1) == 0 or deque1[-1] == "("):
                    answer = "no"
                    break
                else:
                    deque1.pop()



        if len(deque1)!= 0 or len(deque2) != 0:
            answer = "no"
    print(answer)