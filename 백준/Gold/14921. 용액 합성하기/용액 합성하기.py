n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = 98765432101
s, e = 0, n - 1
a, b = -1, -1
while s != e:
    tmp = arr[s] + arr[e]
    if abs(tmp) < m:
        m = abs(tmp)
        a, b = s, e
    if tmp > 0:
        e -= 1
    elif tmp < 0:
        s += 1
    else:
        break
print(arr[a]+arr[b])
