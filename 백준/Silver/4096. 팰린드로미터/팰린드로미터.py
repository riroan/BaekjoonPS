def isPalin(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True
while 1:
    s=input()
    if s == '0':
        break
    l = len(s)
    n = int(s)
    for i in range(n, 10**l):
        t = '0'*(l-len(str(i)))+str(i)
        if isPalin(t):
            print(int(t)-n)
            break