
단어  = input().upper()

case = list(set(단어))
cnt = []

for c in case:
    temp = 단어.count(c)
    cnt.append(temp)

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(case[(cnt.index(max(cnt)))])
