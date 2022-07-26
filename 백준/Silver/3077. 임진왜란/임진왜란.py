n=int(input())
arr=input().split()
brr = input().split()
d = {}
dd ={}
for i in range(n):
    d[arr[i]] = i
    dd[brr[i]] = i
ans = 0
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if d[arr[i]] < d[arr[j]] and dd[arr[i]] < dd[arr[j]]:
            ans+=1
        cnt+=1
print(f"{ans}/{cnt}")
