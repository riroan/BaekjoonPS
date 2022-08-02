def getFail(b):
    lb = len(b)
    fail = [0]*lb
    j = 0
    for i in range(1, lb):
        while j > 0 and b[i] != b[j]:
            j = fail[j-1]
        if b[i] == b[j]:
            j += 1
            fail[i] = j
    return fail
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
b=input()
fail = getFail(b)


if len(b) == 1:
    print(-1)
else:
    if fail[-1] == 0:
        print(-1)
    else:
        pattern = b[:fail[-1]]
        if len(kmp(b, pattern))>2:
            print(pattern)
        else:
            fail = getFail(pattern)
            if fail[-1] == 0:
                print(-1)
            else:
                print(pattern[:fail[-1]])