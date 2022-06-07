n = int(input())
arr = [input() for i in range(n)]
s = int(input())
if s == 1:
    for i in arr:
        print(i)
elif s == 2:
    for i in arr:
        print(i[::-1])
else:
    for i in arr[::-1]:
        print(i)