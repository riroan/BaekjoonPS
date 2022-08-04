n=int(input())
arr = list(map(int, input().split()))
ix = 1
for i in range(n):
    if arr[i] == ix:
        ix+=1
print(n-ix+1)