n,m = map(int, input().split())
arr = []
if n:
    arr = list(map(int, input().split()))
boxes = [0]
for i in arr:
    if boxes[-1] + i <= m:
        boxes[-1]+=i
    else:
        boxes.append(i)
if n == 0:
    print(0)
else:
    print(len(boxes))