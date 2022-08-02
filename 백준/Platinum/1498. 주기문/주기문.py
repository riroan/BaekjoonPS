b = input()
lb = len(b)
fail = [0]*lb
j = 0
for i in range(1, lb):
    while j > 0 and b[i] != b[j]:
        j = fail[j-1]
    if b[i] == b[j]:
        j += 1
        fail[i] = j
ans = []
for i in range(lb):
    if fail[i] == 0:
        continue
    pre = i+1-fail[i]
    if (i+1)%pre == 0:
        print(i+1, (i+1)//pre)
#         ans.append((i+1, (i+1)//pre))
# ans.sort(key=lambda x:(-x[-1],x[0]))
# m = ans[0][1]
# for x,y in ans:
#     if y == m:
#         print(x,y)