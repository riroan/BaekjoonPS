n=int(input())
arr = [list(map(int, input().split()))[:-1] for i in range(n)]
i=1
while True:
    ok = True
    brr = [j[:i] for j in arr]
    m = 0
    for j in brr:
        m = max(m, len(j))
    brr = [j + [0]*(m-len(j)) for j in brr]
    for j in range(n):
        for k in range(j+1, n):
            if brr[j] == brr[k]:
                ok = False
    if ok:
        print(i)
        break
    i+=1