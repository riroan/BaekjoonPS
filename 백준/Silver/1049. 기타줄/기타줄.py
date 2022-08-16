from math import ceil
n,k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(k)]
arr.sort(key=lambda x:x[0])
a = arr[0][0]
arr.sort(key=lambda x:x[1])
b = arr[0][1]
ans1 = ceil(n/6)*a
ans2 = n//6*a + (n-n//6*6)*b
ans3 = n*b
print(min([ans1,ans2,ans3]))