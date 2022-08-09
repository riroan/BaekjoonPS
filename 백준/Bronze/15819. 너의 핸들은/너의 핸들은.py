n,k = map(int,input().split())
arr = [input() for i in range(n)]
arr.sort()
print(arr[k-1])