n = 4000010
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

a,b,d=map(int, input().split())
ans = 0
for i in primes:
    if a<=i<=b:
        if str(d) in str(i):
            ans+=1
print(ans)