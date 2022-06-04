n,l=map(int, input().split())
i = 0
while n:
    i+=1
    if str(l) in str(i):
        continue
    n-=1
print(i)