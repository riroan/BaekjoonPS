n = 40001
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

k=int(input())
dp = [0]*(k+1)

for ix, i in enumerate(primes):
    if i > k:
        continue
    dp[i] += 1
    for j in range(i+1, k+1):
        dp[j] += dp[j-i]
        dp[j]%=123456789
print(dp[-1])
