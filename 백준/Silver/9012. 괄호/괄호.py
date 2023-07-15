
N = int(input())

for i in range(N):
    z = []
    temp = list(input())

    for j in range(len(temp)):
        if temp[j] == "(":
            z.append("(")
        else:
            if (len(z) == 0 ):
                print("NO")
                break
            else:
                z.pop()
    else:
        if len(z) == 0:
            print("YES")
        else:
            print("NO")
