arr = []
try:
    while 1:
        arr+=list(map(int, input().split()))
except:
    pass
arr = arr[1:]
arr = [int(str(i)[::-1])for i in arr]
arr.sort()
for i in arr:
    print(i)