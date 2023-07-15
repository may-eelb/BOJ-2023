import sys

N = int(sys.stdin.readline())
mylist =[]

for i in range(N):
    temp = input()
    mylist.append(temp)

mylist.sort()
mylist = list(set(mylist))


for j in range (1 , 20001):
    for i in range( len(mylist)):
        if ( len(mylist[i]) == j):
            print(mylist[i])