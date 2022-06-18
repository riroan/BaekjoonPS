n,k = map(int, input().split())
arr = [input() for i in range(k)]
d={}
ix = 0
for i in arr:
    d[i] = ix
    ix+=1
brr = []
for i in d:
    brr.append((i, d[i]))
brr.sort(key= lambda x:x[1])
for i in range(min(n,len(brr))):
    print(brr[i][0])