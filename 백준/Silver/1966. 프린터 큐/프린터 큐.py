from collections import deque

N = int(input())

for i in range(N):
    num_doc, target_idx = map(int, input().split())
    p = deque(list(map(int, input().split())))
    idx = deque(list(range(num_doc)))
    ans =[]
    while len(p) :
        if p[0] == max(p):
            p.popleft()
            ans.append(idx.popleft())
        else:
            p.rotate(-1)
            idx.rotate(-1)


    print(ans.index(target_idx) + 1)
