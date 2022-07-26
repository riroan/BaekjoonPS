n=int(input())
e = int(input())
arr = [set() for i in range(n)]
for i in range(e):
    brr = list(map(int, input().split()))[1:]
    brr = [i-1 for i in brr]
    s = set(brr)
    if 0 in s:
        for j in s:
            arr[j].add(i)
    else:
        ss = set()
        for j in s:
            ss |= arr[j]
        for j in s:
            arr[j] = ss.copy()
ans = 0
for i in range(n):
    if len(arr[i]) == len(arr[0]):
        print(i+1)