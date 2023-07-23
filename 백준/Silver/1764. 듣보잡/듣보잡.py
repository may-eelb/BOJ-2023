
N,M = map(int, input().split())
list1 = []
list2 =[]
def find_duplicates_using_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    duplicates = set1.intersection(set2)
    return list(duplicates)

for i in range(N):
    list1.append(input())

for j in range(M):
    list2.append(input())

result = find_duplicates_using_set(list1, list2)
result.sort()

print(len(result))
for temp in result:
    print(temp)