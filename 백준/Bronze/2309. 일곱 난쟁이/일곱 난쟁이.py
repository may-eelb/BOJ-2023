from sys import stdin
input = stdin.readline
ml = []
sum = 0

for i in range(9):
    temp = int(input())
    ml.append(temp)
    sum += temp

for j in range(8):
    for k in range(j+1, 9):
        if (sum - ml[j] - ml[k]) == 100:
            
            t1 = ml[j]
            t2 = ml[k]
            ml.remove(t1)
            ml.remove(t2)
            ml.sort()
            print(*ml, sep = "\n")
            exit()


