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
for test in range(int(input())):
    a=input()
    b=input()
    print(len(kmp(b,a)))