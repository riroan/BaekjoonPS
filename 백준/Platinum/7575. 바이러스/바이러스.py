import sys
input = lambda: sys.stdin.readline().strip()

def kmp(a,b):
    lb = len(b)
    fail = [0]*lb
    j = 0
    for i in range(1, lb):
        while j > 0 and b[i] != b[j]:
            j = fail[j-1]
        if b[i] == b[j]:
            j += 1
            fail[i] = j
    ans = []
    j=0
    for i in range(len(a)):
        while j and a[i] != b[j]:
            j = fail[j-1]
        if a[i] == b[j]:
            if j == lb-1:
                ans.append(i-lb+2)
                j = fail[j]
            else:
                j += 1
    return ans

n,k = map(int, input().split())
arr = []
for i in range(n):
    input()
    arr.append(list(map(int, input().split())))
flag = False
for i in range(len(arr[0]) - k+1):
    ok = True
    pattern = arr[0][i:i+k]
    for j in range(1, n):
        brr = arr[j].copy()
        a = kmp(brr, pattern)
        b = kmp(brr[::-1], pattern)
        if not a and not b:
            ok = False
            break
    flag |= ok
if flag:
    print("YES")
else:
    print("NO")