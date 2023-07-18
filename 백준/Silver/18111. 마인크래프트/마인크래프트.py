
N, M, B = map(int, input().split())

cnt = []
for i in range(N ):
    cnt.append(list(map(int, input().split())))
fflat_list = [item for sublist in cnt for item in sublist]

min_time = 999999999
answer = 0
for key in range(0, 257):
    #print(f'{key} : key')
    flat_list = fflat_list
    ttime = 0
    inven = B

    for i in range(len(flat_list)):
        if (flat_list[i] > key):
            #print(f'{i} 번째 블럭하나 빼기')
            ttime += (flat_list[i]-key)*2
            inven += (flat_list[i]-key)

        else:
            #print(f'{i} 번째 블럭 추가')
            ttime += (key - flat_list[i])
            inven -= (key - flat_list[i] )

    if inven >= 0:
    #print(f'{key} \n {flat_list}')
        if ( ttime <= min_time):
            min_time = ttime
            answer = key


print(f'{min_time} {answer}')
