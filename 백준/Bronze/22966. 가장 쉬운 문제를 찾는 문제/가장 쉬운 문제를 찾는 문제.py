n=int(input())
arr = [input().split() for i in range(n)]
arr.sort(key = lambda x:int(x[1]))
print(arr[0][0])