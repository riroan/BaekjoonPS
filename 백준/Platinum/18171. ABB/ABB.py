def manacher(s):
    n = len(s)
    A = [0] * n
    r = 0
    p = 0
    for i in range(n):
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        else:
            A[i] = 0
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and s[i - A[i] - 1] == s[i + A[i] + 1]:
            A[i] += 1
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return A
n=int(input())
s=list(input())
s = '#'.join(s)
s = '#'+s+'#'
arr = manacher(s)
ix = -1
for i in range(len(arr)-1,-1,-1):
    if arr[i] + i == len(arr)-1:
        ix = i
print(ix-n)