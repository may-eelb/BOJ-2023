#
# N, M = map(int, input().split())
#
case1 = [ ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ]
case2 = [ ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ]



def count_different_elements(arr1, arr2):
    count = 0
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr1[i][j] != arr2[i][j]:
                count += 1
    return count


a = []
N, M = map(int, input().split())


for i in range(N):
    test = list(input())
    a.append(test)

sum = 8*8 # 더 작아지면 갱신

i = 0


while ( i + 8 < N+ 1):
    j = 0
    while (j+8 < M + 1):
        temp = []
        for row in a[i:i + 8]:
            tempp = row[j : j + 8]
            temp.append(tempp)

        tempsum = count_different_elements(case1, temp)
        if ( tempsum < sum):
            sum = tempsum
        j = j + 1
    i = i + 1

i = 0


while ( i + 8 < N + 1):
    j = 0
    while (j + 8 < M+1):
        temp = []
        for row in a[i:i + 8]:
            tempp = row[j:j + 8]
            temp.append(tempp)

        tempsum = count_different_elements(case2, temp)
        if ( tempsum < sum):
            sum = tempsum
        j+=1
    i+=1

print(sum)

