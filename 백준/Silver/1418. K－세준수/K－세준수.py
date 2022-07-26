n = 100010
sieve = [1]*n
sieve[0] = sieve[1] = 0
for i in range(2, n):
    if sieve[i] == 0:
        continue
    for j in range(2*i,n,i):
        sieve[j] = 0
primes = []
for i, v in enumerate(sieve):
    if v:
        primes.append(i)
        
def factorization(n):
    m = 0
    ix = 0
    while n>1:
        while n%primes[ix] == 0:
            n//=primes[ix]
            m = max(m, primes[ix])
        ix+=1
    return m
n=int(input())
k=int(input())
ans = 0
for i in range(1,n+1):
    m = factorization(i)
    if m<=k:
        ans+=1
print(ans)