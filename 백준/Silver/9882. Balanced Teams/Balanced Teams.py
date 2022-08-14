from itertools import combinations
arr = [int(input()) for i in range(12)]
ans = 10**18
for i in combinations([i for i in range(12)], 3):
    for j in combinations([j for j in range(12) if j not in i], 3):
        for k in combinations([k for k in range(12) if k not in i and k not in j], 3):
            l = [l for l in range(12) if l not in i and l not in j and l not in k]
            a = sum([arr[x] for x in i])
            b = sum([arr[x] for x in j])
            c = sum([arr[x] for x in k])
            d = sum([arr[x] for x in l])
            ans =min(ans, max([a,b,c,d])-min([a,b,c,d]))
print(ans)