n, k = map(int, input().split())
arr = list(map(int, input().split()))
u = k*(k-1)//2
arr.sort(reverse=True)
print(sum(arr[:k])-u)