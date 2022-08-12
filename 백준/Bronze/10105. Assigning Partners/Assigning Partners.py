n =int(input())
arr = input().split()
brr =input().split()
d = {}
for i,j in zip(arr, brr):
    d[i] = j
try:
    for i in d:
        a = i
        b =d[i]
        d[a]
        d[b]
        if d[a] != b or d[b] != a:
            assert 0
        if a==b:
            assert 0
    print("good")
except:
    print("bad")