import sys
mod = 1000000009


def pow(x, p):
    ret = 1
    piv = x
    while p:
        if p & 1:
            ret = (ret * piv) % mod
        piv = (piv * piv) % mod
        p >>= 1
    return ret


def berlekamp_massy(x):
    ls, cur = list(), list()
    lf, ld = 0, 0
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + 1 * x[i - j - 1] * cur[j]) % mod
        if (t - x[i]) % mod == 0:
            continue
        if len(cur) == 0:
            cur = [0] * (i + 1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        k = -(x[i] - t) * pow(ld, mod - 2) % mod
        c = [0] * (i - lf - 1)
        c.append(k)
        for j in ls:
            c.append(-j * k % mod)
        if len(c) < len(cur):
            c = c + [0] * (len(cur) - len(c))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    for i in range(len(cur)):
        cur[i] = (cur[i] % mod + mod) % mod
    return cur


def get_nth(rec, dp, n):
    m = len(rec)
    s, t = [0] * m, [0] * m
    s[0] = 1
    if m != 1:
        t[1] = 1
    else:
        t[0] = rec[0]

    def mul(v, w, rec):
        m = len(v)
        t = [0] * (2 * m)
        for j in range(m):
            for k in range(m):
                t[j + k] += v[j] * w[k] % mod
                if t[j + k] >= mod:
                    t[j + k] -= mod
        for j in range(2 * m - 1, m - 1, -1):
            for k in range(1, m + 1):
                t[j - k] += t[j] * rec[k - 1] % mod
                if t[j - k] >= mod:
                    t[j - k] -= mod
        t = t[:m]
        return t

    while n:
        if n & 1:
            s = mul(s, t, rec)
        t = mul(t, t, rec)
        n >>= 1
    ret = 0
    for i in range(m):
        ret += s[i] * dp[i] % mod
    return ret % mod


def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    v = berlekamp_massy(x)
    if len(v) == 0:
        return 0
    return get_nth(v, x, n)


arr = [1, 1, 2, 3, 7, 12, 22, 40, 75, 137, 252, 463,
       853, 1568, 2884, 5304, 9757, 17945, 33006]
brr = [0, 1, 2, 4, 6, 12, 22, 41, 74, 137, 252, 464,
       852, 1568, 2884, 5305, 9756, 17945, 33006]


def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n = int(input())
    print(guess_nth_term(arr, n-1), guess_nth_term(brr, n-1))