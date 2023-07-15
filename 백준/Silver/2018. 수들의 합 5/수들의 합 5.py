start = 1
end = 1

answer = 0

N= int(input())
sum = 1
while (end != N) :

    if sum == N :
        answer += 1
        end += 1
        sum += end
    elif ( sum > N):
        sum -= start
        start += 1

    else :
        end += 1
        sum += end

answer += 1

print(answer)