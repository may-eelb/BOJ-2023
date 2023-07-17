
N = int(input())
people = []
for i in range(N):
    temp = list(map(int, input().split()))
    people.append(temp)

answer = [0] * N

for j in range(N-1):
    #print(f'j : {j}')
    k = j+1
    while k < N:
        if  people[j][0] > people[k][0] and  people[j][1] > people[k][1] :
            answer[k] += 1
        elif people[j][0] < people[k][0] and  people[j][1] < people[k][1] :
            answer[j] += 1
        k += 1

result = [x + 1 for x in answer]
for r in result:
    print(r, end =" ")






