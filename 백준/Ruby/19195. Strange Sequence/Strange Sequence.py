mod = 7340033


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


arr = [1, 2, 4, 4, 6, 10, 12, 14, 22, 26, 30, 44, 56, 70, 98, 130, 162, 216, 292, 358, 470, 628, 792, 1050, 1384, 1788, 2334, 3072, 3974, 5162, 6784, 8786, 11420, 14992, 19484, 25388, 33160, 43262, 56252, 73392, 95798, 124496, 162556, 212048, 275976, 360154, 469694, 611844, 797628, 1040344, 1355550, 1766402, 2304368, 3002354, 3913802, 5103798, 6651808, 1330929, 3964467, 56364, 4526934, 3020079, 3283660, 5845937, 4089463, 6249217, 6173168, 5434618, 6035817, 3277472, 599541, 2502130, 101659, 1046904, 615205, 4310505, 7073937, 1528843, 1573423, 628109, 3338517, 7141678, 6639170,
       7199721, 2508559, 6983719, 3226808, 1362909, 4057445, 5216401, 4789473, 7148607, 3490252, 3859839, 3919928, 4410603, 1774464, 5030371, 3213868, 3673656, 2253480, 162153, 6967672, 6212357, 1488891, 5272969, 2288129, 3900589, 6122846, 6177603, 475903, 151346, 4687899, 1154734, 4168110, 1744680, 1925769, 3198859, 1886183, 702652, 4959058, 6769965, 4832688, 6752128, 5192022, 872961, 2974929, 4528640, 4768052, 929662, 5895668, 7181370, 6213930, 7284455, 594448, 3091509, 5305389, 2707419, 3941867, 1121753, 845827, 3309438, 595600, 781040, 946746, 13034, 2718932, 7085679, 3266476, 5093050]
n=int(input())
print(guess_nth_term(arr, n))