n,k = map(int, input().split())
arr =[list(map(int, input().split())) for i in range(n)]
for i in range(n):
    tmp = []
    for j in arr[i]:
        tmp += [j]*k
    for _ in range(k):
        print(*tmp)