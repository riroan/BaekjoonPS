from collections import defaultdict
n,p,q,x,y = map(int, input().split())
dp = defaultdict(int)
def get(ix):
    global dp
    if ix <= 0:
        return 1
    if dp[ix]:
        return dp[ix]
    dp[ix] = get(ix//p-x) + get(ix//q-y)
    return dp[ix]

print(get(n))