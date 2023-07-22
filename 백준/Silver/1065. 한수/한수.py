
N = int(input())
cnt = 0


def number_to_list(number):
    number_str = str(number)
    num_list = []
    for digit in number_str:
        num_list.append(int(digit))

    return num_list



for i in range(1, N+1):
    tempstr = []
    tempstr = number_to_list(i)
    if len(tempstr) ==1 or len(tempstr) == 2:
        cnt +=1
    elif len(tempstr) == 3:
        if (tempstr[0] - tempstr[1] == tempstr[1] - tempstr[2] ):
            cnt+=1
    else:
        if (tempstr[0] - tempstr[1] == tempstr[1] - tempstr[2] == tempstr[2] - tempstr[3]):
            cnt+=1

print(cnt)