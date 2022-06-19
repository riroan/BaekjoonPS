n=int(input())
arr = [i+1 for i in range(n-1)] + [997]
print(n)
print(*arr)