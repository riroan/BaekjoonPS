import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    arr = []
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        arr.append(s)
    tmp = arr[0]
    s = set()
    for i in arr[1:]:
        s.add(i.split()[-1])
    ans = []
    for i in tmp.split():
        if i not in s:
            ans.append(i)
    print(*ans)