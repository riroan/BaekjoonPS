s = input()
n = len(s)
d = {}


def f(l, r, ss, seq=[]):
    global d
    if l < 0 and r >= n:
        seq+=[ss]
        d[tuple(seq)] = True
    if l >= 0:
        f(l-1, r, s[l]+ss, seq + [ss])
    if r < n:
        f(l, r+1, ss+s[r], seq+[ss])


for i in range(n):
    f(i-1, i+1, s[i])
print(len(d))