n,k=map(int, input().split())
s = input()
t = []
for i in range(n):
    if s[i]=='H':
        t.append(-1)
    else:
        t.append(0)

for i in range(n):
    if t[i] == -1:
        for j in range(-k, k+1):
            if i+j < 0 or i+j>=n:
                continue
            if t[i+j] == 0:
                t[i+j] = 1
                break
cnt = 0
for i in range(n):
    if t[i] == 1:
        cnt+=t[i]
print(cnt)