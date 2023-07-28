from sys import stdin
input = stdin.readline

temp = input().strip()
ttemp = []
ttt =[]
for i in range( len(temp) - 2):
    for j in range( i+1, len(temp)-1):
        ttemp = []
        ttemp.append(temp[i::-1])
        ttemp.append(temp[j:i:-1])
        ttemp.append(temp[:j:-1])
        #print(ttemp)
        ttt.append(ttemp[0]+ttemp[1]+ttemp[2])
        #print(ttt)

ttt.sort()
print(ttt[0])