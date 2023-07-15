N, M = map(int, input().split())
my_list = list(map(int, input().split()))



start_idx = 0
end_idx = 1
answer = 0

Ms = 0


while (start_idx<=end_idx and end_idx <= N):
    Ms = sum(my_list[start_idx:end_idx])
    if (Ms == M):
        answer+=1
        end_idx+=1
    elif (Ms < M ):
        end_idx+=1
    else:
        start_idx+=1

print(answer)