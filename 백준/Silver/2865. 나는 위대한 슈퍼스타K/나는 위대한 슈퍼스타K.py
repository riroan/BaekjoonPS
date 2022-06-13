n, m, k = map(int, input().split())
check = [0]*n
for i in range(m):
    brr = input().split()
    brr = [[int(brr[2*i])-1, float(brr[2*i+1])]for i in range(n)]
    for x,y in brr:
        check[x] = max(check[x],y)
check.sort(reverse=True)
print(round(sum(check[:k]),1))