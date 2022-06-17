n = int(input())
s = list(input())
for i in range(n//2+1):
    if s[i] == '?' and s[n-i-1] == '?':
        s[i] = 'a'
        s[n-i-1] = 'a'
    elif s[i] == '?':
        s[i] = s[n-i-1]
    elif s[n-i-1] == '?':
        s[n-i-1]=s[i]
print(''.join(s))