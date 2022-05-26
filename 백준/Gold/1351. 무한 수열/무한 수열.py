from collections import defaultdict
n,p,q = map(int, input().split())
dp = defaultdict(int)
dp[0] = 1
def get(ix):
    global dp
    if dp[ix]:
        return dp[ix]
    dp[ix] = get(ix//p) + get(ix//q)
    return dp[ix]

print(get(n))