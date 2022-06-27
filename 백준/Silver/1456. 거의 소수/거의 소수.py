n = 10**7+5
sieve = [1]*n
sieve[0] = sieve[1] = 0
for i in range(2, n):
    if sieve[i] == 0:
        continue
    for j in range(2*i, n, i):
        sieve[j] = 0
primes = []
for i, v in enumerate(sieve):
    if v:
        primes.append(i)
cnt = 0
a, b = map(int, input().split())
for p in primes:
    t = p
    while t < 10**14:
        t*=p
        if a<=t<=b:
            cnt+=1
print(cnt)