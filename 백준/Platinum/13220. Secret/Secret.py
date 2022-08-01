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
n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
if kmp(a+a,b):
    print("YES")
else:
    print("NO")