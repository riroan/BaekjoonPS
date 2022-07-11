n=int(input())
ix = 2
sieve = [0]*(n+1)
sieve[0] = sieve[1] = 1
for i in range(2, n+1):
    if sieve[i]:
        continue
    for j in range(i,n+1,i):
        sieve[j] = ix
    ix+=1
print(ix-1)
print(*sieve[1:])