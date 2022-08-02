import sys
def input(): return sys.stdin.readline().strip()


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


n = int(input())
arr = list(map(int, input().split()))
brr = ['#'] * n
crr = []
for i, j in zip(arr, brr):
    crr.append(j)
    crr.append(i)
crr.append('#')
arr = manacher(crr)
for _ in range(int(input())):
    a, b = map(int, input().split())
    if (b-a) % 2 == 0:
        m = (a+b)//2
        a = 2*a-1
        b = 2*b-1
        d = arr[2*m-1]
        if 2*m-1-d < a:
            print(1)
        else:
            print(0)
    else:
        m = (a+b)//2
        d = arr[2*m]
        if 2*m-d <= 2*a-1:
            print(1)
        else:
            print(0)
