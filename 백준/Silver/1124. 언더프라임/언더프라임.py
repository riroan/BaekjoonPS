a,b=map(int, input().split())
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

def f(n):
    ret = 0
    ix = 0
    while n>1:
        while n%primes[ix] == 0:
            n//=primes[ix]
            ret+=1
        ix+=1
    return ret
ans=0
ss = set(primes)
for i in range(a, b+1):
    if f(i) in ss:
        ans+=1
print(ans)