import sys

stack =[]

N = int(sys.stdin.readline())

for i in range(N):
    temp = list(sys.stdin.readline().split())
    if ( len(temp) == 2):  ## push
        stack.append(temp[1])

    elif temp[0] == "pop":
        if ( len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)

    elif temp[0] == "size":
        print(len(stack))
    elif temp[0] == "empty":
        if (len(stack)) == 0:
            print(1)
        else:
            print(0)
    else :
        if (len(stack)) == 0:
            print(-1)
        else:
            print(stack[-1])

