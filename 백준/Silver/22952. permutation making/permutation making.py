n=int(input())
arr = []
for i in range(1, n//2+1):
    arr.append(n-i+1)
    arr.append(i)
    
if n%2:
    arr.append(n//2+1)
print(*arr)