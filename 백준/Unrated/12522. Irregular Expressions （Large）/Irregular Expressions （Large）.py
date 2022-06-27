import sys
input = lambda: sys.stdin.readline().strip()

def check(s):
    cnt = 0
    for i in s:
        if i in 'aeiou':
            cnt+=1
    return cnt

def f(s, n):
    ok = False
    for i in range(2, n//2+1):
        if s[:i] == s[-i:]:
            if check(s[:i]) >= 2 and check(s[i:-i]) >= 1:
                ok = True
                break
    return ok

for test in range(int(input())):
    s = input()
    n = len(s)
    ok = False
    for i in range(1, n+1):
        for j in range(n-i+1):
            ok|=f(s[j:j+i], i)
    print(f"Case #{test+1}: ",end="")
    if ok:
        print("Spell!")
    else:
        print("Nothing.")